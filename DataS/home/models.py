from django.db import models
from tinymce.models import HTMLField

# Create your models here.
from db.base_model import BaseModel
from home.emus import hotTableTypes,tableStatus,dbType


class HotTablesManager(models.Manager):
    '''常用表模型管理器'''
    def get_table_by(self, table_subtype=str, limit=None, sort='default'):
        if sort == 'length':
            order_by = ('table_name',)
        else:
            order_by('-create_time',)
        
        # 查询数据
        hotTablse_li = self.filter(table_subtype=table_subtype).order_by(*order_by)
        
        # 对查询结果集进行限制h
        if limit :
            hotTablse_li= hotTablse_li[:limit]
        return hotTablse_li
            
    


class HotTables(BaseModel):
    """常用表模型"""
    hotTableType_choices = ((k,v) for k,v in hotTableTypes.items())
    tableStatus_choices = ((k,v) for k,v in tableStatus.items())
    dbType_choices = ((k,v) for k,v in dbType.items())

    table_id = models.IntegerField(verbose_name='表id')
    table_name =models.CharField(max_length=50, verbose_name='表名')
    db_name = models.CharField(max_length=10,verbose_name='表的库名')    
    table_subtype = models.CharField(default='other', max_length=10, choices=hotTableType_choices,verbose_name='表业务子类型')
    table_type = models.CharField(default='other', max_length=10, verbose_name='表业务类型')
    db_type = models.CharField(default='other',max_length=10, choices=dbType_choices, verbose_name='数据库类型')
    desc = models.CharField(max_length=128, verbose_name='表的简介')
    detail = HTMLField(verbose_name='表的详情')
    status = models.SmallIntegerField(default=1, choices=tableStatus_choices, verbose_name='表的状态')
    
    objects =HotTablesManager()
    
    def __str__(self):
        return self.table_name
    
    class Meta:
        db_table = 's_tables'
        verbose_name = '常用表'
        verbose_name_plural = verbose_name 
        
        
    
                                  