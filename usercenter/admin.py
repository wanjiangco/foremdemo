from django.contrib import admin
from models import ActivateCode
# Register your models here.
class ActivateCodeadmin(admin.ModelAdmin):
    list_display = ('owner','code','expire_timestamp','creat_time')
    list_filter = ('owner',)
admin.site.register(ActivateCode,ActivateCodeadmin)