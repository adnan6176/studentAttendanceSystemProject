from django.contrib import admin

# Register your models here.
from . models import Student
from . models import Attendance

from . models import classID

# class AttendanceAdmin(admin.ModelAdmin):
#     readonly_fields =('submit_date')



admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(classID)
# admin.site.register(AttendanceAdmin)