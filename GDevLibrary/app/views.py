from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.core.mail import send_mail

from .forms import UserForm, LoginForm


def UserRegisterView(request):
    user = request.user if request.user.is_authenticated else None
    template_name = 'app/register.html'
    if request.method == 'POST': 
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False) 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            send_mail(
             'Welcome to GDevLibrary',
             'Click on this lick for your email authetizatation',
             settings.EMAIL_HOST_USER,
              [email, settings.EMAIL_HOST_USER],
              fail_silently = False
             )

            return redirect('login')
    else:
        form = UserForm()

    content= {
        'form':form,
        'user':user 
        }

    return render(request, template_name, content)

def UserLoginView(request):
    user = request.user if request.user.is_authenticated else None
    print(user)
    template_name = 'app/login.html'
    if request.method ==  'POST':
        form =  LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["name"]
            password = form.cleaned_data["password"]

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')
    else:
        form = LoginForm()
    content= {
        'form':form,
        'user':user 
        }

    return render(request, template_name, content)



def home(request):
    """Renders the home page."""
    user = request.user if request.user.is_authenticated else None
    return render(
        request,
        'app/main.html',
        {'user':user})

def main_unity(request):
    user = request.user if request.user.is_authenticated else None
    print(user)
    return render(
        request,
       'app/unity_main.html',
       {'user':user})

def main_unreal(request):
    user = request.user if request.user.is_authenticated else None
    print(user)
    return render(
        request,
        'app/unreal_main.html',
        {'user':user})

def main_cry(request):
    user = request.user if request.user.is_authenticated else None
    print(user)
    return render(
        request,
       'app/cry_main.html',
       {'user':user})
