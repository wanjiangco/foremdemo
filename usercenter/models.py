
#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ActivateCode(models.Model):
    owner=models.ForeignKey(User,verbose_name='用户')
    code=models.CharField(u'激活码',max_length=100)
    expire_timestamp=models.DateTimeField(u'过期时间')
    creat_time=models.DateTimeField(auto_now_add=True)
    modify_time=models.DateTimeField(auto_now=True)
