from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'pages/dashboard.html')


def contact(request):
	return HttpResponse('contact page')


def rule(request):
	return HttpResponse('rules')


def student_detail(request):
	return render(request, 'pages/student_detail.html')

# Create your views here.
