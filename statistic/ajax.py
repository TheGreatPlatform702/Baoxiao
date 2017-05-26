from const import *
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.template.loader import render_to_string
from django.utils import simplejson
from registration.models import CommonUser
from django.contrib.auth.models import User
from django.contrib import auth
from statistic.form import SearchForm
import datetime
from django.db.models import Q
from statistic.models import BaoXiaoTable

def createDateRangeQ(start_date, end_date):
    print start_date, end_date
    if start_date and end_date:
        return Q(date__lte = datetime.date(start_date)) & Q(date__gte = datetime.date(end_date))
    elif start_date:
        return Q(date__lte = datetime.date(start_date))
    elif end_date:
        return Q(date__gte = datetime.date(end_date))
    return Q()

def createUserQ(student_name, student_number):
    uesr = []; common_user = []
    if student_name:
        user = User.objects.filter(username = student_name)
    if student_number:
        common_user = CommonUser.objects.filter(student_number = student_number)
    
    if student_number:
        if common_user:
            return Q(user = common_user[0].user)
        else: return Q()
    elif student_name:
        if user:
            return Q(user__in = user)
        else: return  Q()

@dajaxice_register
def search(request, form):
    form = SearchForm(deserialize_form(form))
    statu = 0
    result = None
    if form.is_valid():
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        q_date_range = createDateRangeQ(start_date, end_date)
        name = form.cleaned_data['student_name']
        stno = form.cleaned_data['student_number']
        q_name_stno = createUserQ(name, stno)

        baoxiao_tables = BaoXiaoTable.objects.filter(q_date_range and q_name_stno)
        print baoxiao_tables
        baoxiao_tables_html = render_to_string('statistic/widgets/result_list.html', {
            'result_list': baoxiao_tables
        })
        result = baoxiao_tables_html
    else:
        statu = 1
    
    context = {
        'statu': statu,
        'html': result
    }
    return simplejson.dumps(context)