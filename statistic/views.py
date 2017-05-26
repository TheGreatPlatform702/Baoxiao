# Create your views here.

# Create your views here.
from const import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from statistic.form import SearchForm
from registration.models import Administrator, CommonUser

def home(request):
    form = SearchForm()
    context = {"username": request.user.username, "form": form}
    return render(request, 'statistic/stat.html', context)
