from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^article/(?P<article_id>\d+)/$', views.article_page,name='article_page'),
    url(r'^article/edit/(?P<article_id>\d+)$', views.article_edit_page,name='article_edit_page'),
    url(r'^article/edit/action/$', views.article_edit_page_action, name='article_edit_page_action'),

]