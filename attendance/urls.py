from django.contrib import admin
from django.urls import path , include
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('dashboard/<str:class_id>', views.dashboard, name='dashboard'),
    path('attendance/<str:class_id>', views.attendance, name='attendance'),
    path('viewAttendance/', views.viewAttendance, name='viewAttendance'),
    path('currentPage/', views.currentPage, name='currentPage'),
    path('makeAttendance/', views.makeAttendance, name='makeAttendance'),
]