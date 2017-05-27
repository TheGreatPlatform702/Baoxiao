#coding=utf8
from const import *
from django import  forms
from django.forms import ModelForm
from statistic.models import BaoXiaoTable, DetailMoney

# class BaoxiaoForm(forms.Form):
#     office_supplies_keywords = forms.CharField(widget = forms.TextInput)
#     office_supplies_bill_number = forms.IntegerField(widget = forms.TextInput)
#     office_supplies_money = forms.FloatField(widget = forms.TextInput)

#     book_keywords = forms.CharField(widget = forms.TextInput)
#     book_bill_number = forms.IntegerField(widget = forms.TextInput)
#     book_money = forms.FloatField(widget = forms.TextInput)

#     printing_keywords = forms.CharField(widget = forms.TextInput)
#     printing_bill_number = forms.IntegerField(widget = forms.TextInput)
#     printing_money = forms.FloatField(widget = forms.TextInput)

#     post_keywords = forms.CharField(widget = forms.TextInput)
#     post_bill_number = forms.IntegerField(widget = forms.TextInput)
#     post_money = forms.FloatField(widget = forms.TextInput)

#     phone_keywords = forms.CharField(widget = forms.TextInput)
#     phone_bill_number = forms.IntegerField(widget = forms.TextInput)
#     phone_money = forms.FloatField(widget = forms.TextInput)

#     internet_keywords = forms.CharField(widget = forms.TextInput)
#     internet_bill_number = forms.IntegerField(widget = forms.TextInput)
#     internet_money = forms.FloatField(widget = forms.TextInput)

#     traffic_keywords = forms.CharField(widget = forms.TextInput)
#     traffic_bill_number = forms.IntegerField(widget = forms.TextInput)
#     traffic_money = forms.FloatField(widget = forms.TextInput)

#     maintenance_keywords = forms.CharField(widget = forms.TextInput)
#     maintenance_bill_number = forms.IntegerField(widget = forms.TextInput)
#     maintenance_money = forms.FloatField(widget = forms.TextInput)

#     conference_keywords = forms.CharField(widget = forms.TextInput)
#     conference_bill_number = forms.IntegerField(widget = forms.TextInput)
#     conference_money = forms.FloatField(widget = forms.TextInput)

#     material_keywords = forms.CharField(widget = forms.TextInput)
#     material_bill_number = forms.IntegerField(widget = forms.TextInput)
#     material_money = forms.FloatField(widget = forms.TextInput)

#     # cooperation = models.ForeignKey(DetailMoney, verbose_name = u'科研协作费', related_name = 'cooperation_set')
#     # thirdpart = models.ForeignKey(DetailMoney, verbose_name = u'委托业务费', related_name = 'thirdpart_set')
#     # school_management = models.ForeignKey(DetailMoney, verbose_name = u'学校管理费', related_name = 'school_management_set')
#     # base_management = models.ForeignKey(DetailMoney, verbose_name = u'基层管理费', related_name = 'base_management_set')
#     # water_electric = models.ForeignKey(DetailMoney, verbose_name = u'水电费', related_name = 'water_electric_set')
#     # other = models.ForeignKey(DetailMoney, verbose_name = u'其他事务费', related_name = 'other_set')
#     # rent = models.ForeignKey(DetailMoney, verbose_name = u'租赁费', related_name = 'rent_set')
#     # specific_facility = models.ForeignKey(DetailMoney, verbose_name = u'专用设备购置', related_name = 'specific_facility_set')
#     # software = models.ForeignKey(DetailMoney, verbose_name = u'软件购置费', related_name = 'software_set')
#     # hotel = models.ForeignKey(DetailMoney, verbose_name = u'住宿费', related_name = 'hotel_set')


class SmallBaoxiaoForm(ModelForm):
    class Meta:
        model = DetailMoney
        widgets = {
            'keyword': forms.TextInput(attrs={'class':'form-control'}),
            'bill_amount': forms.TextInput(attrs={'class':'form-control'}),
            'money': forms.TextInput(attrs={'class':'form-control'})
        }

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

