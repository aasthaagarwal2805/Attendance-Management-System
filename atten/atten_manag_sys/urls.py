from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home ),
    path('rule/',views.rule),
    path('contact/',views.contact),
    path('student_detail/', views.student_detail),
    path('stu_login/', views.student_login),
    path('educational/', views.educational),
    path('communication/', views.communication),
    path('employe_login/', views.employee_login),

]
