from django.shortcuts import render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


def home(request):
	return render(request, 'pages/dashboard.html')


def contact(request):
	return HttpResponse('contact page')


def rule(request):
	return render(request, 'pages/rules.html')


def student_detail(request):
	return render(request, 'pages/student_detail.html')


def student_login(request):
	# form= UserCreationForm()
	# context={'form': form}
	return render(request, 'pages/stu_login.html')

def communication(request):
	return render(request, 'pages/communicational.html')


def educational(request):
	return render(request, 'pages/educational_details.html')

def employee_login(request):
	return render(request, 'pages/employe_login.html')


# def leave(request):
# 	form=leaveForm()
# 	context={'form':form}
# 	return render(request, 'pages/leave.html', context)



# # Create your views here.
