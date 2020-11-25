from django.urls import path

from django.contrib.auth import views as auth_views

from . import views 


urlpatterns = [
    path('', views.home , name='dashboard' ),
    path('rule/',views.rule, name='rules'),
    path('contact/',views.contact , name='contacts'),
    path('student_detail/', views.student_detail, name='student-detail'),
    path('stu_login/', views.student_login, name='student-login'),
    path('logout/', views.logoutUser, name='logout'),
    path('educational/', views.educational, name='education'),
    path('communication/', views.communication, name='communicational'),
    path('employe_login/', views.employee_login, name='employee-login'),
    # path('leave/', views.leave),


    # path('reset_password/', auth_views.PasswordResetView.as_view() name="reset_password"),

    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view() name="password_reset_done"),

    # path('reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view() name="password_reset_confirm"),
    
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view() name="password_reset_complete"),

]
