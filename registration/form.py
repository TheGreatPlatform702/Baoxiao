#coding=utf8
from const import *
from django import  forms
from django.forms import ModelForm

class LoginForm(forms.Form):
    student_number = forms.IntegerField(widget = forms.TextInput)
    password = forms.CharField(widget = forms.PasswordInput)
    role = forms.ChoiceField()
    def __init__(self,*args,**kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["role"].choices = ROLE_CHOICE

class RegisterForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput)
    student_number = forms.IntegerField(widget = forms.TextInput)
    password = forms.CharField(widget = forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)

