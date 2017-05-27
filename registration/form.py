#coding=utf8
from const import *
from django import  forms
from django.forms import ModelForm

class LoginForm(forms.Form):
    student_number = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    role = forms.ChoiceField(widget = forms.Select(attrs={'class':'form-control'}))
    def __init__(self,*args,**kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["role"].choices = ROLE_CHOICE

class RegisterForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
    student_number = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))

