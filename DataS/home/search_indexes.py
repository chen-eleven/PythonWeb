# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:04:52 2019

@author: chen
"""

from haystack import indexes
from home.models import Tables,TableDetails


# 指定对于某个类的某些数据建立索引, 一般类名:模型类名+Index
class TablesIndex(indexes.SearchIndex, indexes.Indexable):
    # 指定根据表中的哪些字段建立索引:比如:商品名字 商品描述
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Tables

    def index_queryset(self, using=None):
        return self.get_model().objects.all()