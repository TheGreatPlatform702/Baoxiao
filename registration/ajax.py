from const import *
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.template.loader import render_to_string
from django.utils import simplejson
from registration.form import LoginForm, RegisterForm
from registration.views import canLogin
from registration.models import CommonUser
from django.contrib.auth.models import User
from django.contrib import auth

@dajaxice_register
def login(request, form):
    form = LoginForm(deserialize_form(form))
    statu = 0
    context = {}
    if form.is_valid():
        st_no = int(form.cleaned_data['student_number'])
        password = form.cleaned_data['password']
        role = int(form.cleaned_data['role'])
        if not canLogin(request, st_no, password, role): statu = 1
    else:
        statu = 1
    context['statu'] = statu
    return simplejson.dumps(context)

@dajaxice_register
def register(request, form):
    form = RegisterForm(deserialize_form(form))
    statu = 0
    context = {}
    if form.is_valid():
        name = form.cleaned_data['name']
        st_no = int(form.cleaned_data['student_number'])
        password = form.cleaned_data['password']
        try:
            user = User(username = st_no, first_name = name)
            user.set_password(password)
            user.save()
            common_user = CommonUser(user = user, student_number = st_no)
            common_user.save()
            user = auth.authenticate(username = st_no, password = password)
            if user: auth.login(request, user)
        except Exception, e:
            print e
            statu = 1
    else:
        statu = 1
    context['statu'] = statu
    return simplejson.dumps(context)
