from django.contrib import admin

# Register your models here.
from models import Article

class Articleadmin(admin.ModelAdmin):
    list_display = ('status','title','owner','creat_time','modify_time')
    list_filter = ('block',)
    search_fields = ['title','content',]
admin.site.register(Article,Articleadmin)
