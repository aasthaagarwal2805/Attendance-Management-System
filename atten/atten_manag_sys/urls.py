from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home ),
    path('rule/',views.rule),
    path('contact/',views.contact),
    path('student_detail/', views.student_detail)
    # path('communication/', views.communication_detail),
]
