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
from statistic.models import BaoXiaoTable

def home(request):
    form = SearchForm()
    result_list = BaoXiaoTable.objects.all().order_by('-date')[0:20]
    context = {
        "username": request.user.username, 
        "form": form, "result_list": result_list,
        "role": 'commonuser'
    }
    return render(request, 'statistic/stat.html', context)
