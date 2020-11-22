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

# def communication_detail(request):
# 	return render(request, 'pages/communication.html')

# # Create your views here.
