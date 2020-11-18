from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home ),
    path('rule/',views.rule),
    path('contact/',views.contact),
]
