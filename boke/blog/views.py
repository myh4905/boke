
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog import models


def index(request):
    articles = models.Article.objects.all()
    #这里是取所有，如果取某一个article = models.Article.objects.get(pk=1)
    return render(request, 'index.html', {'articles': articles})

def article_page(request, article_id):        #根据博客id获取博客内容
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})

def article_edit_page(request,article_id):
    # str方法将参数转化为字符串，避免因传递类型差异引起的错误
    # 0代表是新增博客，否则是编辑博客，编辑博客时需要传递博客对象到页面并显示
    if str(article_id) == '0':
        return render(request, 'article_edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_edit_page.html',{'article':article})

def article_edit_page_action(request):
    title = request.POST.get('title', '默认标题')     ##get是根据参数名称从form表单页获取内容
    content = request.POST.get('content', '默认内容')
    ##保存数据
    models.Article.objects.create(title=title, content=content)
    ##数据保存完成，返回首页
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

