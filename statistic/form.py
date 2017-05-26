#coding=utf8
from const import *
from django import  forms
from django.forms import ModelForm

class SearchForm(forms.Form):
    start_date = forms.DateField(widget = forms.TextInput(attrs={
        "class": "datetimepicker form-control",
        "label": "开始日期"
    }), required = False)
    end_date = forms.DateField(widget = forms.TextInput(attrs={
        "class": "datetimepicker form-control",
        "label": "结束日期"
    }), required = False)
    student_name = forms.CharField(widget = forms.TextInput(attrs={
        "class": "form-control",
        "label": "姓名"
    }), required = False)
    student_number = forms.IntegerField(widget = forms.TextInput(attrs={
        "class": "form-control",
        "label": "学号"
    }), required = False)

