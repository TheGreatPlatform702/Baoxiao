#coding=utf8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DetailMoney(models.Model):
    keyword = models.CharField(verbose_name = u'关键字', max_length = 100, blank = True, null = True)
    bill_amount = models.IntegerField(verbose_name = u'单据数', blank = False, null = False, default = 0)
    money = models.FloatField(verbose_name = u'金额', blank = False, null = False, default = 0)

    class Meta:
        verbose_name = u'具体发票数据'
        verbose_name_plural = u'具体发票数据'
    
    def __unicode__(self):
        return u'%d张发票，总共%f元(%s)' % (self.bill_amount, self.money, self.keyword)

class BaoXiaoTable(models.Model):
    date = models.DateField(verbose_name = u'最后修改日期', blank = False, null = False, auto_now = True)
    user = models.ForeignKey(User, verbose_name = u'用户')
    office_supplies = models.ForeignKey(DetailMoney, verbose_name = u'日常办公用品', related_name = 'office_supplies_set')
    book = models.ForeignKey(DetailMoney, verbose_name = u'书报杂志订阅费', related_name = 'book_set')
    printing = models.ForeignKey(DetailMoney, verbose_name = u'印刷费', related_name = 'printing_set')
    handling_charge = models.ForeignKey(DetailMoney, verbose_name = u'手续费', related_name = 'handling_set')
    post = models.ForeignKey(DetailMoney, verbose_name = u'邮电费', related_name = 'post_set')
    phone = models.ForeignKey(DetailMoney, verbose_name = u'电话费', related_name = 'phone_set')
    internet = models.ForeignKey(DetailMoney, verbose_name = u'网络通讯费', related_name = 'internet_set')
    traffic = models.ForeignKey(DetailMoney, verbose_name = u'交通费', related_name = 'traffic_set')
    maintenance = models.ForeignKey(DetailMoney, verbose_name = u'维护费', related_name = 'maintenance_set')
    conference = models.ForeignKey(DetailMoney, verbose_name = u'会议费', related_name = 'conference_set')
    material = models.ForeignKey(DetailMoney, verbose_name = u'专用材料费', related_name = 'material_set')
    cooperation = models.ForeignKey(DetailMoney, verbose_name = u'科研协作费', related_name = 'cooperation_set')
    thirdpart = models.ForeignKey(DetailMoney, verbose_name = u'委托业务费', related_name = 'thirdpart_set')
    school_management = models.ForeignKey(DetailMoney, verbose_name = u'学校管理费', related_name = 'school_management_set')
    base_management = models.ForeignKey(DetailMoney, verbose_name = u'基层管理费', related_name = 'base_management_set')
    water_electric = models.ForeignKey(DetailMoney, verbose_name = u'水电费', related_name = 'water_electric_set')
    other = models.ForeignKey(DetailMoney, verbose_name = u'其他事务费', related_name = 'other_set')
    rent = models.ForeignKey(DetailMoney, verbose_name = u'租赁费', related_name = 'rent_set')
    specific_facility = models.ForeignKey(DetailMoney, verbose_name = u'专用设备购置', related_name = 'specific_facility_set')
    software = models.ForeignKey(DetailMoney, verbose_name = u'软件购置费', related_name = 'software_set')
    hotel = models.ForeignKey(DetailMoney, verbose_name = u'住宿费', related_name = 'hotel_set')

    total_bills = models.IntegerField(verbose_name = u'总单据数', blank = False, null = False, default = 0)
    total_money = models.FloatField(verbose_name = u'总额', blank = False, null = False, default = 0.0)

    class Meta:
        verbose_name = u'报销单'
        verbose_name_plural = u'报销单'

    def __unicode__(self):
        return u'%s %s(%d张发票，总共%d元)' % (self.date.isoformat(), self.user.username, self.total_bills, self.total_money)