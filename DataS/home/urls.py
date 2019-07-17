# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 22:27:35 2019

@author: chen
"""
from home import views
from django.urls import path

app_name = 'home'

urlpatterns = [
        path('', views.index, name='index'),   # 首页
        ]