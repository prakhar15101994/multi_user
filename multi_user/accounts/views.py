from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render

from accounts.forms import LoginForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from accounts.models import MyUser

# Create your views here.

def register_page(request):
	forms=RegisterForm()
	if request.method=='POST':
		form=RegisterForm(request.POST)
		if form.is_valid():
			obj=form.save(commit=False)
			obj.save()
			return redirect('login')
	else:
		return render(request, 'accounts/register_page.html', {'form':forms})
    

def login_page(request):
	if request.user.is_authenticated:
		return redirect('profile')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('profile')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login_page.html', context)

def profile_page(request):
    data=MyUser.objects.all()
    return render(request, 'accounts/profile_page.html', {'datas':data})

def logout_user(request):
	logout(request)
	return redirect('login')