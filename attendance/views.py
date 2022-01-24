from typing import ContextManager
from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.db import IntegrityError
from django.utils import timezone
import datetime

from django.http import HttpResponse
from django.http import HttpResponseRedirect 

from .forms import AttendanceForm, classForm

from .models import Student, Attendance, TimeTable , classID, Profile

from django.utils.dateparse import parse_date

def home(request):
    return render(request,'attendance/home.html')

# Create your views here.

def signupuser(request):


    if (request.method=='GET'):
        context = {'form' : UserCreationForm}
        return render(request,'attendance/signupuser.html',context)
    else:
        
        if(request.POST['password1']==request.POST['password2']):
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
                # return render(request,'todo/signupuser.html',{'msg':'this is post request password are  matching'})
            except IntegrityError:
                context = {'msg':'user name already taken'}
                return render(request,'todo/signupuser.html',context)        
        else:
            return render(request,'attendance/signupuser.html',{'msg':'this is post request password are not matching'})


def loginuser(request):
    if (request.method=='GET'):
        context = {'form': AuthenticationForm}
        return render(request,'attendance/login.html',context)
    else:
       
       user=authenticate(request, username=request.POST['username'], password = request.POST['password'])
       if user is None:
           context = {'form': AuthenticationForm,'error':'incorrect username or password '}
           return render(request ,'attendance/login.html',context)
       else:
        login(request,user)
        return redirect('currentPage') 


def logoutuser(request):
    if (request.method =='POST'):
        logout(request)
        return redirect('home')
        
def dashboard(request,class_id):
    students = Student.objects.all()
    class_x = get_object_or_404( classID , id = class_id)
    students = Student.objects.filter( class_name = class_x)
    context = {'students': students}

    if request.method=='POST':
        date_str = request.POST.get('date')
        date1 = parse_date(date_str)
        print("printing request")
        # date = datetime.datetime.strptime(request.POST.get('date'),"Y-mm-dd").date()

        print("printing student id")
        for student in students:
            temp = request.POST[str(student.id)]
            print(temp)
            v =  Attendance(student_id = student , present = temp, teacher = request.user , date_present= date1)
            v.save()
       
    print("stop printing student")
    return render(request,'attendance/dashboard.html',context)
    



def attendance(request, class_id):
    students = Student.objects.all()
    class_x = get_object_or_404( classID , id = class_id)
    students = Student.objects.filter( class_name = class_x)
    attendances = Attendance.objects.filter( student_id__in =students)
    context = {'students' : students,'class_x' : class_x, 'attendances' : attendances}
    return render(request,'attendance/attendance.html',context)


def currentPage(request):
    if request.method == 'POST':
        temp = request.POST['className']
        return redirect('dashboard',temp)
    else:
        className = classID.objects.all()
        context = {'className':className}
        return render(request,'attendance/currentPage.html',context)



def viewAttendance(request):
    if request.method == 'POST':
        date_str = request.POST.get('date')
        date_str = str(date_str)
        date_str = parse_date(date_str)

        temp = request.POST['className']
        temp = get_object_or_404( classID , id = temp)
        students = Student.objects.filter( class_name = temp)
        attendances = Attendance.objects.filter( student_id__in =students, date_present = date_str)
        context = {'students' : students,'class_x' : temp , 'attendances' : attendances,'date' :date_str}
        return render(request,'attendance/attendance.html',context)



def makeAttendance(request):
    if request.method=='GET':
        date_str = request.GET.get('date')
        date_str = str(date_str)
        print(date_str)
        date_str = parse_date(date_str)
        print('############3')
        
        mydate = date_str
        temp = request.GET['className']
        temp = get_object_or_404( classID , id = temp)
        students = Student.objects.filter( class_name = temp)
        context = {'students': students , 'date1':mydate, 'class' : temp}
        return render(request,'attendance/dashboard.html',context)
        # attendances = Attendance.objects.filter( student_id__in =students, date_present = date_str)

    if request.method == 'POST':
        date_str = request.POST.get('date1')
        print('###############')
        print(date_str)
        date_str = str(date_str)
        print('###############')
        date_str = parse_date(date_str)
        print(date_str)
        mydate = date_str
        temp = request.GET['className']
        temp = get_object_or_404( classID , id = temp)
        students = Student.objects.filter( class_name = temp)
        context = {'students': students , 'date1':mydate, 'class' : temp}

        for student in students:
            # temp = request.POST[str(student.id)]
            # v =  Attendance(student_id = student , present = temp, teacher = request.user , date_present= mydate)
            # v.save()

            temp = request.POST[str(student.id)]

            x = Attendance.objects.filter(student_id = student,date_present= mydate).count()
            y = Attendance.objects.filter(student_id = student,date_present= mydate)
            if (x == 0):
                v =  Attendance(student_id = student , present = temp, teacher = request.user , date_present= mydate)
                v.save()
            else:
                y.update(student_id = student , present = temp, teacher = request.user , date_present= mydate)



        className = classID.objects.all()
        context = {'className':className}
        return render(request,'attendance/currentPage.html',context)

def newpage(request):
    teachers = Profile.objects.all()
    context = {'teachers' : teachers}
    return render(request,'attendance/orange/index.html',context)


def profilepage(request,id):
    teachers = Profile.objects.get(id=id)
    context = {'teacher':teachers}
    return render(request,'attendance/orange/profile.html',context)


def teacherProfilePage(request):
    teachers = Profile.objects.all()
    context = {'teachers':teachers}
    return render(request,'attendance/orange/clients.html',context)

def blankPage(request):
    teachers = Profile.objects.all()
    context = {'teachers':teachers}
    return render(request,'attendance/orange/blank-page.html',context)

def redirectDashboard(request):
    return redirect('newpage')


def employeeDashboard(request,id):
    teacher = Profile.objects.get(id=id)
    timetables = TimeTable.objects.filter(teacher = teacher)
    todayDate =  datetime.datetime.today()
    today = datetime.datetime.today().weekday()
    today_tts = TimeTable.objects.filter(teacher = teacher , day=today)
    tomorrow_tts = TimeTable.objects.filter(teacher = teacher , day=(today+1)%7)

    next7day = TimeTable.objects.filter(teacher = teacher , day=(today+2)%7)
    today = today+3
    for x in range(4):
        today = (int(today)+x)%7
        tts = timetables.filter(day = today).order_by('day')
        next7day = next7day | tts

    dayList =['','Tuesday', 'Wednessday','Thursday','Friday','Saturday','Sunday']


    today_day = todayDate.strftime("%A")
    today_date = todayDate.date()
    context = {'teacher':teacher ,'timetables' : timetables , 
                'today_tts' : today_tts , 
                'tomorrow_tts' : tomorrow_tts,
                'today_date' : today_date,
                'today_day': today_day,
                'next7days' :next7day,
                } 

    return render(request,'attendance/orange/employee-dashboard.html',context)


def loginuser1(request):
    if (request.method=='GET'):
        context = {'form': AuthenticationForm}
        return render(request,'attendance/orange/login.html',context)
    else:
       
       user=authenticate(request, username=request.POST['username'], password = request.POST['password'])
       if user is None:
           context = {'form': AuthenticationForm,'error':'incorrect username or password '}
           return render(request ,'attendance/orange/login.html',context)
       else:
        login(request,user)

        id = user.profile.id
        url = f"/employeeDashboard/{id}"
        return redirect(url) 
        
     





def forgetpassword(request):
    context={}
    return render(request,'attendance/orange/forgot-password.html',context)


def register(request):
    if (request.method=='GET'):
        context = {}
        return render(request,'attendance/orange/register.html',context)
    else:
        
        if(request.POST['password1']==request.POST['password2']):
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
                # return render(request,'todo/signupuser.html',{'msg':'this is post request password are  matching'})
            except IntegrityError:
                context = {'myMsg':'user name already taken'}
                return render(request,'attendance/orange/register.html',context)        
        else:
            context = {'myMsg':'Passwords are not matching'}
            return render(request,'attendance/orange/register.html',context)

def signoutuser(request):
    # if (request.method =='POST'):
        logout(request)
        return redirect('/login1/')


def viewAttendances(request):
    if request.method == 'POST':
        temp = request.POST['className']
        return redirect('dashboard',temp)
    else:
        className = classID.objects.all()
        context = {'className':className}
    return render(request,'attendance/viewAttendence.html',context)





