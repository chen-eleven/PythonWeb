# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:25:30 2019

@author: chen
"""
from django.urls import path 
from nlp import views

app_name = 'nlp'
urlpatterns = [
    path('lda/', views.lda, name='lda'), # lda

    ]