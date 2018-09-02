from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserLoginForm
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, UserSelectionForm
from .models import *
from company.models import *
from django.contrib.auth.models import User,UserManager
from django.core.files.storage import FileSystemStorage
# Create your views here.

def is_member(user):
    return user.groups.filter(name='Coordinators').exists()

def index(request):
	context = {
	'display' : 'hello world'
	}
	return render(request,'index.html',{})

def login_page(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			password = userObj['password']
			user = authenticate(username=username,password = password)
			if user is not None:
				
				
				login(request,user)
				user_check = UserProfile.objects.filter(user = user)

				user_check = user_check.first()
				print(user_check.isPlaced)
				if(user_check.isPlaced):
					return render(request,'congrats.html',{})
				if(is_member(user)):
					messages.success(request,'Admin Login Succesfull!!')
					return redirect('homeCoordinator')
				messages.success(request,'Logged in Succesfully!!')
				return redirect('homeStudent')
			else:
				raise forms.ValidationError('Looks like username/password is wrong!')
	else:
		form = UserLoginForm()
	return render(request,'login.html',{'form':form})


@login_required(login_url='login/')
def logout_page(request):
    
    logout(request)
    messages.success(request,'Logged out Succesfully!!')
    return redirect('/')


@login_required(login_url='login/')
def home(request):

	user = UserProfile.objects.filter(user = request.user)
	user = user.first()
	cgpa = float(user.cgpa)
	branch = user.branch
	companies = Companies.objects.filter(cgpa__lte=cgpa, br_allowed = branch)


	return render(request,'home.html',{'companies':companies})

@user_passes_test(is_member)
@login_required(login_url='login/')
def coordinator_home(request):
	user = UserProfile.objects.filter(user = request.user)
	user = user.first()
	cgpa = float(user.cgpa)
	branch = user.branch
	companies = Companies.objects.filter(cgpa__lte=cgpa, br_allowed = branch)
	return render(request,'home_coordinator.html',{'companies':companies})


@login_required(login_url='login/')
def update_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES)
		if form.is_valid():
			userObj = form.cleaned_data
			cgpa = userObj['cgpa']
			user = UserProfile.objects.filter(user = request.user)
			user = user.first()
			user.cgpa = cgpa
			user.save()
			user = request.user
			messages.success(request,'Updated Succesfully!!')
			if(is_member(user)):
				return redirect('homeCoordinator')
			return redirect('homeStudent')
	else:
	 	form = UserProfileForm()
	return render(request,'user_profile.html',{'form':form}) 


def register_page(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			email =  userObj['email']
			password =  userObj['password']
			firstname =  userObj['first_name']
			lastname =  userObj['last_name']
			regnum = userObj['regnum']
			branch = userObj['branch']
			course = userObj['course']
			contact = userObj['contact']
			if UserProfile.objects.filter(regNum = regnum).count() > 0:
				return render(request, 'register.html', {'error' : 'This Registration Number Has Already Been Registered', 'form' : form})
			
			elif User.objects.filter(username=username).count() == 0 :
				user = User.objects.create_user(username = username ,email= email)
				user.set_password(password)
				user.first_name = firstname
				user.last_name = lastname
				user.save()
				# user = authenticate(username = username, password = password)
				login(request,user)
				profile = UserProfile.objects.create(user = request.user)
				profile.first = firstname
				profile.last = lastname
				profile.regNum = regnum
				profile.branch = branch
				profile.course = course
				profile.contact = contact
				profile.save()
				messages.success(request,'Registered Succesfully!!')
				return redirect('homeStudent')
			else:
				return render(request, 'register.html',{'error': 'This Username/Email is not available!', 'form' : form})
             	# return render(request, 'register.html',{'error': 'This Username/Email is not available!', 'form' : form})

	else:
	 	form = UserRegistrationForm()

	return render(request, 'register.html', {'form' : form})

@user_passes_test(is_member)
@login_required(login_url='login/')
def placed(request):
	if request.method == 'POST':
		form = UserSelectionForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			regnum = userObj['regnum']
			user= UserProfile.objects.filter(regNum = regnum)
			user = user.first()
			user.isPlaced = True
			user.save()
			return redirect('placed')
		
	else:
		form = UserSelectionForm()
		return render(request, 'placed.html', {'form':form})
