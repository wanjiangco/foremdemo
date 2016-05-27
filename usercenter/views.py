#coding:utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from article.models import Block
from django.shortcuts import render
import uuid
import datetime
from models import ActivateCode
from django.core.mail import send_mail

def register(request):
    error=''
    if request.method=='GET':
        return render_to_response('usercenter_register.html',{},context_instance=RequestContext(request))
    else:
        username=request.POST['username'].strip()
        email=request.POST['email'].strip()
        password=request.POST['password'].strip()
        re_password=request.POST['re_password'].strip()
        if not username or not email or not password:
            error='任何字段不能为空'
        if password != re_password:
            error='两次密码不一致'
        if User.objects.filter(username=username).count() > 0:
            error='用户已存在'
        if not error:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.is_active=False
            user.save()

            new_code=str(uuid.uuid4()).replace('-','')
            expire_time=datetime.datetime.now()+datetime.timedelta(days=2)
            code_recode=ActivateCode(owner=user,code=new_code,expire_timestamp=expire_time)
            code_recode.save()

            activate_link="http://%s%s" %(request.get_host(),reverse('usercenter_activate',args=[new_code]))
            send_mail(u'python部落激活邮件',u'激活地址：%s' %  activate_link , '454890130@qq.com', [email],fail_silently=False)
        else:
            return render_to_response('usercenter_register.html',{'error':error},context_instance=RequestContext(request))
        return redirect(reverse('login'))


def activate(request,code):
    query=ActivateCode.objects.filter(code=code,expire_timestamp__gte=datetime.datetime.now())
    if query.count()>0:
        code_record=query[0]
        code_record.owner.is_active=True
        code_record.owner.save()
        return HttpResponse(u'激活成功')
    else:
        return HttpResponse(u'激活失败')


