#coding:utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Block(models.Model):
    block_name=models.CharField(u'板块名称',max_length=20)
    discribe=models.CharField(u'板块描述',max_length=30)
    admin_name=models.ForeignKey(User,verbose_name='管理员')
    creat_time=models.DateTimeField(auto_now_add=True)
    modify_time=models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.block_name
    class Meta:
        verbose_name='板块'
        verbose_name_plural='板块'
