# Create your views here.
# Create your views here.
from const import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from bills.form import SmallBaoxiaoForm

def home(request):
    forms = []
    for i in range(len(ITEMS)):
        forms.append((ITEMS[i][0], ITEMS[i][1], SmallBaoxiaoForm()))
    context = {"forms": forms, "username": request.user.username}
    return render(request, 'baoxiao/baoxiao.html', context)


# def loginRedirect(request):
# 	redirect_url = "/home"
# 	return HttpResponseRedirect(redirect_url)

# def logoutRedirect(request):
#     redirect_url = ""
#     return HttpResponseRedirect(redirect_url)