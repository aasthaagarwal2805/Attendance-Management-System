from atten_manag_sys.models import student_user
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='student-login')
def home(request):
	return render(request, 'pages/dashboard.html')

@login_required(login_url='student-login')
def contact(request):
	return HttpResponse('contact page')

@login_required(login_url='student-login')
def rule(request):
	return render(request, 'pages/rules.html')

@login_required(login_url='student-login')
def student_detail(request):
    stu_details = student_user.objects.all()
    x = {'stu_details': stu_details}
    return render(request, 'pages/student_detail.html', x)


def student_login(request):
	# form= UserCreationForm()
	# context={'form': form}

	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method=='POST':
			username=request.POST.get('username')
			password= request.POST.get('password')
		

			user= authenticate(request,username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username or Password is incorrect')
				return render(request,'pages/stu_login.html' )
	context={}
	return render(request, 'pages/stu_login.html')


def leave(request):
	leaves= leave.objects.all()
	y = {'leaves': leaves}
	return render(request, 'pages/leave.html', y)


	
@login_required(login_url='student-login')
def communication(request):
	return render(request, 'pages/communicational.html')

@login_required(login_url='student-login')
def educational(request):
	return render(request, 'pages/educational_details.html')

def employee_login(request):
	return render(request, 'pages/employe_login.html')

@login_required(login_url='student-login')
def logoutUser(request):
	logout(request)
	return redirect('student-login')
	


# def leave(request):
# 	form=leaveForm()
# 	context={'form':form}
# 	return render(request, 'pages/leave.html', context)



# # Create your views here.
