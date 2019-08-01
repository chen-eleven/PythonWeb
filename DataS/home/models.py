from django.db import models
from tinymce.models import HTMLField

# Create your models here.
from db.base_model import BaseModel
from home.emus import hotTableTypes,tableStatus,dbType
from home.emus import db_name_all


class HotTablesManager(models.Manager):
    '''常用表模型管理器'''
    def get_table_by(self, table_subtype=str, limit=None, sort='default'):
        if sort == 'length':
            order_by = ('table_name',)
        else:
            order_by('-tabel_name',)
        
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
        db_table = 's_hot_tables'
        verbose_name = '常用表'
        verbose_name_plural = verbose_name 
        

class TablesManager(models.Manager):
    '''表模型管理器'''
    def get_table_by_id(self, table_id=int):
        # 查询数据
        table = self.filter(table_id=table_id)       
        # 对查询结果集进行限制h
        return table
    def get_tables_by_type(self,db_type=1, db_name=str, sort='table_name'):
        # 查询数据
        table = self.filter(db_type=db_type).filter(db_name=db_name).order_by(sort) 
        # 对查询结果集进行限制h
        return table
    def get_db_name_all(self,db_type='hive'):
        """获取去重所有库名"""
        #因为库不易变动，还是直接写死成一个文件，不浪费数据库IO、
        return db_name_all[db_type]
        
                
    

class Tables(BaseModel):
    '''父级表'''
    tableStatus_choices = ((k,v) for k,v in tableStatus.items())
    dbType_choices = ((k,v) for k,v in dbType.items())

    table_id = models.IntegerField(verbose_name='表id',primary_key=True)    
    table_name =models.CharField(max_length=50, verbose_name='表名')
    db_name = models.CharField(max_length=10,verbose_name='表的库名')        
    table_type = models.CharField(default=None, max_length=10, verbose_name='表业务类型')
    db_type = models.CharField(default='other',max_length=10, choices=dbType_choices, verbose_name='数据库类型')
    desc = models.CharField(max_length=128, verbose_name='表的简介')
    
    objects = TablesManager()
    
    def __str__(self):
        return self.table_name
    
    class Meta:
        db_table = 's_tables'
        verbose_name = '表库'
        verbose_name_plural = verbose_name


class TableDetailsManager(models.Manager):
    """子级表模型管理器"""
    def get_table_by_id(self, table_id=int):
        table_detail = self.filter(table_id=table_id)
        return table_detail
    

class TableDetails(BaseModel):
    """子级表详细信息"""
    #table_id = models.IntegerField( verbose_name='tableid', )
    table_id = models.ForeignKey(Tables, verbose_name='tableid', on_delete=models.CASCADE)
    clo_id = models.IntegerField(default=None, verbose_name='列id')
    clo_name = models.CharField(default=None, max_length=50,verbose_name='列名')
    field_type = models.CharField(default=None, max_length=150,verbose_name='字段类型')
    level = models.SmallIntegerField(default=0, verbose_name='字段等级,默认0普通')
    comment = models.CharField(default=None, max_length=600, verbose_name='表的简介')
    
    objects = TableDetailsManager()
    
    def __str__(self):
        return str(self.table_id)    # 必须返回string
    
    class Meta:
        db_table = 's_table_details'
        verbose_name = '子表详细信息'
        verbose_name_plural = verbose_name


    
    
    
    