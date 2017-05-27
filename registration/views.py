# Create your views here.
from const import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from registration.form import LoginForm, RegisterForm
from registration.models import Administrator, CommonUser

def isRightRole(request, users, password):
    if users:
        user = auth.authenticate(username = users[0].user.username, password = password)
        if user:
            auth.login(request, user)
            return True
        else:
            return False
    else:
        return False

def canLogin(request, st_no, password, role):
    statu = 0
    if role == ADMIN:
        admin = Administrator.objects.filter(student_number = st_no)
        return isRightRole(request, admin, password)
    else:
        common_user = CommonUser.objects.filter(student_number = st_no)
        return isRightRole(request, common_user, password)

def isAdministrator(request):
    admin = Administrator.objects.filter(user = request.user)
    if admin: return True
    return False

def jump(request):
    if isAdministrator(request):
        return HttpResponseRedirect('/statistic')
    else:
        return HttpResponseRedirect('/baoxiao/list')

def haveLogined(request):
    if request.user.is_authenticated():
        return True
    else:
        return False

def home(request):
    if haveLogined(request):
        return jump(request)
    else:
        return HttpResponseRedirect('/login')

def login(request):
    if haveLogined(request):
        return jump(request)
    else:
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'registration/login.html', context)

def register(request):
    if haveLogined(request):
        return jump(request)
    else:
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'registration/register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

# def loginRedirect(request):
# 	redirect_url = "/home"
# 	return HttpResponseRedirect(redirect_url)

# def logoutRedirect(request):
#     redirect_url = ""
#     return HttpResponseRedirect(redirect_url)