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
from statistic.models import BaoXiaoTable
from django.template.loader import render_to_string

def create(request):
    forms = []
    for i in range(len(ITEMS)):
        forms.append((ITEMS[i][0], ITEMS[i][1], SmallBaoxiaoForm()))
    context = {
        "forms": forms, 
        "username": request.user.first_name,
    }
    return render(request, 'baoxiao/baoxiao.html', context)

def showList(request):
    baoxiao_tables = BaoXiaoTable.objects.filter(user = request.user).order_by('-date', '-id')
    # html = render_to_string('bills/widgets/table_list.html', baoxiao_tables)
    context = {
        'baoxiao_tables': baoxiao_tables,
        'username': request.user.first_name,
        "role": 'commonuser'
    }
    return render(request, 'baoxiao/baoxiao_list.html', context)

def modify(request, bid):
    baoxiao_table = BaoXiaoTable.objects.get(id = bid)
    form = generateForms(baoxiao_table)
    forms = []
    for i in range(len(ITEMS)):
        forms.append((ITEMS[i][0], ITEMS[i][1], form[i]))
    context = {
        'forms': forms,
        'username': request.user.first_name,
        'id': baoxiao_table.id
    }
    return render(request, 'baoxiao/baoxiao.html', context)

def generateForms(baoxiao):
    form = []
    form.append(SmallBaoxiaoForm(instance = baoxiao.office_supplies))
    form.append(SmallBaoxiaoForm(instance = baoxiao.book))
    form.append(SmallBaoxiaoForm(instance = baoxiao.printing))
    form.append(SmallBaoxiaoForm(instance = baoxiao.handling_charge))
    form.append(SmallBaoxiaoForm(instance = baoxiao.post))
    form.append(SmallBaoxiaoForm(instance = baoxiao.phone))
    form.append(SmallBaoxiaoForm(instance = baoxiao.internet))
    form.append(SmallBaoxiaoForm(instance = baoxiao.traffic))
    form.append(SmallBaoxiaoForm(instance = baoxiao.maintenance))
    form.append(SmallBaoxiaoForm(instance = baoxiao.conference))
    form.append(SmallBaoxiaoForm(instance = baoxiao.material))
    form.append(SmallBaoxiaoForm(instance = baoxiao.cooperation))
    form.append(SmallBaoxiaoForm(instance = baoxiao.thirdpart))
    form.append(SmallBaoxiaoForm(instance = baoxiao.school_management))
    form.append(SmallBaoxiaoForm(instance = baoxiao.base_management))
    form.append(SmallBaoxiaoForm(instance = baoxiao.water_electric))
    form.append(SmallBaoxiaoForm(instance = baoxiao.other))
    form.append(SmallBaoxiaoForm(instance = baoxiao.rent))
    form.append(SmallBaoxiaoForm(instance = baoxiao.specific_facility))
    form.append(SmallBaoxiaoForm(instance = baoxiao.software))
    form.append(SmallBaoxiaoForm(instance = baoxiao.hotel))
    return form


# def loginRedirect(request):
# 	redirect_url = "/home"
# 	return HttpResponseRedirect(redirect_url)

# def logoutRedirect(request):
#     redirect_url = ""
#     return HttpResponseRedirect(redirect_url)