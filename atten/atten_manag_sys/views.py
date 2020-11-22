from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'pages/dashboard.html')


def contact(request):
	return HttpResponse('contact page')


def rule(request):
	return render(request, 'pages/rules.html')


def student_detail(request):
	return render(request, 'pages/student_detail.html')


def student_login(request):
	return render(request, 'pages/student_login.html')

def communication(request):
	return render(request, 'pages/communicational.html')


def educational(request):
	return render(request, 'pages/educational_details.html')

def employee_login(request):
	return render(request, 'pages/employe_login.html')



# # Create your views here.
