from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home , name='dashboard' ),
    path('rule/',views.rule, name='rules'),
    path('contact/',views.contact , name='contacts'),
    path('student_detail/', views.student_detail, name='student-detail'),
    path('stu_login/', views.student_login, name='student-login'),
    path('educational/', views.educational, name='education'),
    path('communication/', views.communication, name='communicational'),
    path('employe_login/', views.employee_login, name='employee-login'),
    # path('leave/', views.leave),

]
