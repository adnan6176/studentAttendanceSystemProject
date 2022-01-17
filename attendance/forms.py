from django.forms import ModelForm, fields
from .models import Attendance, classID

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ['date_present']

class classForm(ModelForm):
    class Meta:
        model = classID
        fields = ['className']