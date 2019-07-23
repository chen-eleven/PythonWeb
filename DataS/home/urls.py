# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:27:35 2019

@author: chen
"""
from home import views
from django.urls import path,re_path

app_name = 'home'

urlpatterns = [
        path('', views.index, name='index'),   # 首页
        #re_path('tables/10003/', views.detail, name='detail'), # 详情页
        re_path('home/(?P<table_id>[0-9]+)/', views.detail, name='detail'), # 详情页
        ]