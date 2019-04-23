from django.contrib import admin

# Register your models here.

from .models import Article




admin.site.site_header = '我的博客'#网站页头
admin.site.site_title = '我的博客系统'  #设置页面标题
admin.site.index_title = '欢迎来到我的博客MIS'  #设置首页标语




admin.site.register(Article)