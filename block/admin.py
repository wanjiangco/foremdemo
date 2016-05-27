from django.contrib import admin

# Register your models here.
from models import Block

class Blockadmin(admin.ModelAdmin):
    list_display = ('block_name','admin_name','discribe','creat_time')
    list_filter = ('admin_name',)
admin.site.register(Block,Blockadmin)
