from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis.serializers import json

from blog import models


def index(request):

    articles = models.BokeInfo.objects.all()
    #这里是取所有，如果取某一个article = models.Article.objects.get(pk=1)
    return render(request, 'index.html', {'articles': articles})

def article_page(request, article_id):
    #根据博客id获取博客内容
    article = models.BokeInfo.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})

def article_edit_page(request,article_id):

    title = request.POST.get('title', '默认标题')  ##get是根据参数名称从form表单页获取内容
    content = request.POST.get('content', '默认内容')
    # str方法将参数转化为字符串，避免因传递类型差异引起的错误
    # 0代表是新增博客，否则是编辑博客，编辑博客时需要传递博客对象到页面并显示
    if str(article_id) == '0':
        if not all([title,content]):
            return HttpResponse("不能为空")
        return render(request, 'article_edit_page.html')


    article = models.BokeInfo.objects.get(pk=article_id)
    return render(request, 'article_edit_page.html',{'article':article})

def article_edit_page_action(request):

    title = request.POST.get('title', '默认标题')     ##get是根据参数名称从form表单页获取内容
    content = request.POST.get('content', '默认内容')
    print(title)
    article_id = request.POST.get('article_id_hidden', '0')##隐藏参数，参数是在web中定义

    ##保存数据
    if str(article_id) == '0':
        if not all([title,content]):
            return HttpResponse("不能为空")
        models.BokeInfo.objects.create(btitle=title,bcontent=content,bpub_date=datetime.now().strftime('%Y-%m-%d'))
        ##数据保存完成，返回首页

        articles = models.BokeInfo.objects.all()
        article_list=[]
        for article in articles:
            article_dict={
                'btitle':article.btitle
            }
            article_list.append(article_dict)

        return render(request, 'index.html', {'article_list': article_list})

    article = models.BokeInfo.objects.get(pk=article_id)
    article.title = title
    article.content = content

    if not all([article.title, article.content]):
        return HttpResponse("不能为空")
    article.save()

    return render(request, 'article_page.html', {'article': article})


def del_article(request,article_id):

    try:
        article = models.BokeInfo.objects.get(id=article_id)
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")
