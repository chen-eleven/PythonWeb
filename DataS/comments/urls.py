# -*- coding: utf-8 -*-
from django.urls import re_path 
from comments import views

app_name = 'comments'
urlpatterns = [
    re_path('getcomm/(?P<table_id>[0-9]+)/', views.get_comments, name='getcomm'), # 评论内容
    re_path('^addcomm/(?P<table_id>[0-9]+)/', views.add_comments,name='addcomm'),
    re_path('submcomm/(?P<table_id>[0-9]+)/', views.subm_comments, name='submit'),

    ]