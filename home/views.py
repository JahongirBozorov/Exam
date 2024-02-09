from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from user.models import MyUser


def index(request):
    return render(request, "home.html")

@login_required(login_url="/login")
def home(request):
    return render(request, "home_join.html")

@login_required(login_url="/login")
def home_admin(request):
    return render(request, "home_joinAdmin.html")

@login_required(login_url="/login")
def register(request):
    if request.method == 'POST':
        new_user = MyUser.objects.create(
            phone_number=request.POST.get('phone_number'),
        )
        new_user.set_password(request.POST.get('password'))
        new_user.save()
        return redirect('home_admin',)
    return render(request, "register.html")
def login(request):
    if request.method == 'POST':
        user = authenticate(phone_number=request.POST.get('phone_number'),
                            password=request.POST.get('password'))
        if user:
            auth_login(request, user)
            # set user-specific data in the session
            request.session['phone_number'] = user.phone_number
            if user.is_superuser:
                return redirect('home_admin',)
            return redirect('home',)
        else:
            return HttpResponse("Invalid user")
    return render(request, "login.html")
