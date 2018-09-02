from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from .models import *
from authentication1.views import *
from .forms import AddCompaniesForm
# Create your views here.

User = settings.AUTH_USER_MODEL



@user_passes_test(is_member)
@login_required(login_url='login/')
def add_companies(request):
	if request.method == 'POST':
		form = AddCompaniesForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			user = request.user
			name = userObj['name']
			ctc = userObj['ctc']
			cgpa = float(userObj['cgpa'])
			br_allowed = userObj['br_allowed']
			add = Companies.objects.create(user= user ,name = name, ctc = ctc, cgpa = cgpa, br_allowed = br_allowed)
			return redirect('add')			
             	
	else:
	 	form = AddCompaniesForm()

	return render(request, 'add_companies.html', {'form' : form})


@login_required(login_url='login/')
def add_applications(request,company_id):
	comp_id = int(company_id)
	user = request.user
	regnum = UserProfile.objects.filter(user = user)
	regnum = regnum.first()
	regnum = regnum.regNum
	name = user.first_name + ' ' + user. last_name +' - ' +str(regnum)
	comp = Companies.objects.filter(id = comp_id)
	comp = comp.first()
	applied = Applicants.objects.filter(user = user)
	for apply in applied:
		if apply.company == comp:
			messages.success(request,'')
			return redirect('homeStudent')
	Applicants.objects.create(user = user,name=name, company=comp)
	messages.success(request,'Applied Succesfully!!')
	return redirect('add')

@user_passes_test(is_member)
@login_required(login_url='login/')
def delete_company(request,company_id):
	comp = int(company_id)
	company = Companies.objects.filter(id = comp)
	company.delete()
	messages.success(request,'Company Deleted Succesfully!!')
	return redirect('handling')


@user_passes_test(is_member)
@login_required(login_url='login/')
def handling_comapnies(request):
	context = {
	'companies':Companies.objects.filter(user = request.user)
	}

	return render(request,'handling_companies.html',context)

@user_passes_test(is_member)
@login_required(login_url='login/')
def details(request,company_id):
	comp = int(company_id)
	company = Companies.objects.filter(id = comp)
	company = company.first()
	context = {
	'name' : company.name,
	'applicants' : Applicants.objects.filter(company = company)
	}
	return render(request,'details_page.html',context)
	


