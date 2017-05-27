from const import *
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.template.loader import render_to_string
from django.utils import simplejson
from registration.models import CommonUser
from django.contrib.auth.models import User
from bills.form import SmallBaoxiaoForm
from django.contrib import auth
from statistic.models import BaoXiaoTable

@dajaxice_register
def baoxiao(request, forms, bid):
    forms = [ SmallBaoxiaoForm(deserialize_form(x)) for x in forms]
    statu = -1
    for i in range(len(forms)):
        if not forms[i].is_valid():
            statu = i
            break
    print statu
    if statu == -1:
        total_bills = 0
        total_money = 0
        for form in forms:
            total_bills += form.cleaned_data['bill_amount']
            total_money += form.cleaned_data['money']
        if bid:
            baoxiao_table = BaoXiaoTable.objects.get(id = bid)
        else:
            baoxiao_table = BaoXiaoTable(user = request.user)
        baoxiao_table.office_supplies = forms[0].save()
        baoxiao_table.book = forms[1].save()
        baoxiao_table.printing = forms[2].save()
        baoxiao_table.handling_charge = forms[3].save()
        baoxiao_table.post = forms[4].save()
        baoxiao_table.phone = forms[5].save()
        baoxiao_table.internet = forms[6].save()
        baoxiao_table.traffic = forms[7].save()
        baoxiao_table.maintenance = forms[8].save()
        baoxiao_table.conference = forms[9].save()
        baoxiao_table.material = forms[10].save()
        baoxiao_table.cooperation = forms[11].save()
        baoxiao_table.thirdpart = forms[12].save()
        baoxiao_table.school_management = forms[13].save()
        baoxiao_table.base_management = forms[14].save()
        baoxiao_table.water_electric = forms[15].save()
        baoxiao_table.other = forms[16].save()
        baoxiao_table.rent = forms[17].save()
        baoxiao_table.specific_facility = forms[18].save()
        baoxiao_table.software = forms[19].save()
        baoxiao_table.hotel = forms[20].save()
        baoxiao_table.total_bills = total_bills
        baoxiao_table.total_money = total_money
        baoxiao_table.save()

    context = {
        'statu': statu
    }
    return simplejson.dumps(context)

# @dajaxice_register
# def login(request, form):
#     form = LoginForm(deserialize_form(form))
#     statu = 0
#     context = {}
#     if form.is_valid():
#         st_no = int(form.cleaned_data['student_number'])
#         password = form.cleaned_data['password']
#         role = int(form.cleaned_data['role'])
#         if not canLogin(request, st_no, password, role): statu = 1
#     else:
#         statu = 1
#     context['statu'] = statu
#     return simplejson.dumps(context)
