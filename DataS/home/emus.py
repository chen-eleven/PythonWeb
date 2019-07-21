# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:46:31 2019

@author: chen
"""

rn = 1
order = 2
report = 3
other = 4

hotTableTypes ={
        'rn' :'埋点数据',
        'order' : '订单数据',
        'report' : '报表数据',
        'other' : '用户及设备属性及其他',}

dbType = {
       'mysql' : 'Mysql数据库',
       'hive' : 'Hive数据库',
       'otherdb' :'其他数据库',}
tableStatus = {
        0 : '下线',
        1 : '正常',
        2 : '其他异常'}