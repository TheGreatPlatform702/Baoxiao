#coding=utf8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Administrator(models.Model):
    user = models.ForeignKey(User)
    student_number = models.IntegerField(verbose_name = u'学号', blank = False, null = False, default = 0, primary_key = True)

    class Meta:
        verbose_name = u'管理员'
        verbose_name_plural = u'管理员'

    def __unicode__(self):
        return self.user.first_name

class CommonUser(models.Model):
    user = models.ForeignKey(User)
    student_number = models.IntegerField(verbose_name = u'学号', blank = False, null = False, default = 0, primary_key = True)

    class Meta:
        verbose_name = u'普通用户'
        verbose_name_plural = u'普通用户'

    def __unicode__(self):
        return self.user.username