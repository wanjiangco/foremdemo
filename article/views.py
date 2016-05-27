#coding:utf-8
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your views here.
from models import Article
from models import Block
from django.contrib.auth.decorators import login_required

def article_list(request,block_id):
    block_id=int(block_id)
    bloc=Block.objects.get(id=block_id)
    articles=Article.objects.filter(block=bloc).order_by('-modify_time')
    return render_to_response('article_list.html',{'articles':articles,'blocks':bloc},context_instance=RequestContext(request))

def article_detail(request,article_id):
    article_id=int(article_id)
    article=Article.objects.get(id=article_id)
    block=Block.objects.get(block_name=article.block)
    if request.method=='GET':
        return render_to_response('article_detail.html',{'article':article,'blocks':block},context_instance=RequestContext(request))

@login_required
def article_create(request,block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    if request.method=='GET':
        return render_to_response('article_create.html',{'blocks':block},context_instance=RequestContext(request))
    else:
        title=request.POST['title'].strip()
        content=request.POST['content'].strip()
        if not title or not content:
            messages.add_message(request,messages.ERROR,u'标题内容均不能为空')
            return render_to_response('article_create.html',{'blocks':block,'title':title,'content':content},context_instance=RequestContext(request))
        owner=User.objects.all()[0]
        new_article=Article(block=block,owner=owner,title=title,content=content)
        new_article.save()
        messages.add_message(request,messages.INFO,u'发表文章成功!')
        return redirect(reverse('article_list',args=[block.id]) )

