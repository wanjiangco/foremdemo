from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
# Create your views here.

from models import Block
def block_list(request):
    blocks=Block.objects.all().order_by('-id')
    if request.method=='GET':
        return render_to_response('block_list.html',{'blocks':blocks},context_instance=RequestContext(request))
