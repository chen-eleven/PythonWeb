# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 07:38:26 2019

@author: chen
"""

from django.db import models

class BaseModel(models.Model):
    '''模型抽象基类'''
    create_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=TabError, null=True, verbose_name='更新时间')

    class Meta:
        abstract = True