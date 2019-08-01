# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:30:47 2019

@author: chen
"""

from django.urls import path

from report import views

app_name='report'
urlpatterns = [
    path('bitest/', views.bar, name='bar'),    # 柱状图
    path('runtime/', views.bar_time_filter, name='runtime'),
    path('echartsapi/', views.ajaxapi, name='ajax')
]
