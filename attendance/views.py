from typing import ContextManager
from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.db import IntegrityError
from django.utils import timezone

from .forms import AttendanceForm, classForm

from .models import Student, Attendance , classID

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
            temp = request.POST[str(student.id)]
            print(temp)
            v =  Attendance(student_id = student , present = temp, teacher = request.user , date_present= mydate)
            v.save()

        className = classID.objects.all()
        context = {'className':className}
        return render(request,'attendance/currentPage.html',context)
        