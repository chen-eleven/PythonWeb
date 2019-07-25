# -*- coding: utf-8 -*-
from django.urls import re_path 
from comments import views

app_name = 'comments'
urlpatterns = [
    re_path('(?P<table_id>[0-9]+)/', views.new_comment, name='comment'), # 评论内容
    ]