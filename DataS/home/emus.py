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

db_name_all = {
        'hive': ["ad",
"ali_parquet_trans",
"antarmy",
"app",
"bus_dw",
"datest",
"default",
"device",
"dmn",
"dwa",
"ezviz_basic",
"ezviz_bigdata",
"ezviz_temp",
"intelligent",
"meta",
"ods",
"open",
"openapi",
"sds_ad",
"sds_ai",
"sds_antarmy",
"sds_app",
"sds_app_rn",
"sds_cloud",
"sds_dclog",
"sds_ddns",
"sds_device",
"sds_ezviz",
"sds_i",
"sds_intelligent",
"sds_mall",
"sds_ms",
"sds_open",
"sds_opensdk",
"sds_other",
"sds_passenger",
"sds_record",
"sds_s",
"sds_saas",
"sds_stream",
"sds_studio",
"sds_supportserver",
"sds_user",
"stage",
"stage_dclog",
"stage_mysql",
"stage_omm",
"studio",
"tag",
"test",
"user_tag",],
        'mysql' : ['ad','datest', 'dwa', 'report','stage', 'test'],
        'otherdb' : []
        }