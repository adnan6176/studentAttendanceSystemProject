from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class classID(models.Model):
    classCode = models.CharField(max_length=2,blank=True, null=True)
    className = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        str_name =  self.className  
        return str_name


class Student(models.Model):
    class_choice = [
    ("N" ,"Nurserry"),
    ("L", 'LKG'),
    ("U","UKG"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ]

    name = models.CharField(max_length=30)
    # class_name = models.CharField(blank=True, max_length=2,choices=class_choice)
    class_name =  models.ForeignKey(classID,on_delete= models.CASCADE, default="", blank=True, null=True)
    roll_number = models.IntegerField(blank=True)
    enroll_teacher = models.ForeignKey(User,on_delete= models.CASCADE, default="", blank=True, null=True)


    class Meta:
        unique_together = ['class_name', 'roll_number']

    def __str__(self):
        str_name =  self.name  
        return str_name


class Attendance(models.Model):
    student_id = models.ForeignKey(Student,on_delete= models.CASCADE, default="")
    present = BooleanField()
    
    # date_present = models.DateTimeField(auto_now_add=True, blank=True)
    date_present = models.DateField(  blank=True,null=True)
    submit_date  = models.DateTimeField( auto_now_add=True, blank=True,null=True)
    teacher =  models.ForeignKey(User,on_delete= models.CASCADE, default="", blank=True, null=True)
    

