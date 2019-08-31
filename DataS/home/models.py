from tinymce.models import HTMLField
from django.db import models
# Create your models here.
from db.base_model import BaseModel
from django.utils import timezone
from home.emus import hotTableTypes,tableStatus,dbType,partStatus,linkStatus
# from home.emus import db_name_all


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
        db_name_all_t = self.filter(db_type=db_type).values_list('db_name').distinct()
        
        db_name_all=sorted([i[0] for i in db_name_all_t])

        #return db_name_all[db_type]
        return db_name_all
        
                
    

class Tables(BaseModel):
    '''父级表'''
    tableStatus_choices = ((k,v) for k,v in tableStatus.items())
    dbType_choices = ((k,v) for k,v in dbType.items())
    havepart_choices = ((k,v) for k,v in partStatus.items())
    linktype_choices = ((k,v) for k,v in linkStatus.items())

    table_id = models.IntegerField(verbose_name='表id',primary_key=True)   
    table_name =models.CharField(default=None, max_length=100, verbose_name='表名')
    db_name = models.CharField(default=None, max_length=30,verbose_name='表的库名')        
    table_type = models.CharField(default=None, max_length=10, verbose_name='表业务类型')
    db_type = models.CharField(default='other',max_length=10, choices=dbType_choices, verbose_name='数据库类型')
    create_user = models.CharField(default=None, null=True, max_length=10, verbose_name='建表人')
    link_type = models.CharField(default=None, null=True, max_length=15, choices=linktype_choices, verbose_name="内外表")
    desc = models.CharField(max_length=300,default=None, null=True, verbose_name='表的简介')
    last_modified_time = models.DateTimeField(default=timezone.now, null=True, verbose_name='最后一次修改时间')
    last_modified_by = models.CharField(default=None, null=True, max_length=10, verbose_name='最后修改人')
    hdfs_path = models.CharField(default=None, null=True, max_length=300, verbose_name='hdfs路径')
    numfiles = models.IntegerField(default=None, null=True, verbose_name='文件个数')
    numrows = models.IntegerField(default=None, null=True, verbose_name='总行数')
    totalsize = models.CharField(default=None, null=True, max_length=50, verbose_name='hdfs文件大小')
    have_part = models.SmallIntegerField(default=0,choices=havepart_choices, verbose_name='是否存储')
    max_part = models.CharField(default=None, null=True, max_length=12, verbose_name='最大dt')
    min_part = models.CharField(default=None, null=True, max_length=12, verbose_name='最小dt')
    
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
        table_detail = self.filter(table_id=table_id).order_by('clo_id')
        return table_detail
    

class TableDetails(BaseModel):
    """子级表详细信息"""
    #table_id = models.IntegerField( verbose_name='tableid', )
    table_id = models.ForeignKey(Tables, verbose_name='tableid', on_delete=models.CASCADE)
    clo_id = models.IntegerField(default=None, verbose_name='列id')
    clo_name = models.CharField(default=None, max_length=50,verbose_name='列名')
    field_type = models.CharField(default=None, null=True, max_length=150,verbose_name='字段类型')
    level = models.SmallIntegerField(default=0, verbose_name='字段等级,默认0普通')
    comment = models.CharField(default=None, null=True, max_length=600, verbose_name='表的简介')
    
    objects = TableDetailsManager()
    
    def __str__(self):
        return str(self.table_id)    # 必须返回string
    
    class Meta:
        db_table = 's_table_details'
        verbose_name = '子表详细信息'
        verbose_name_plural = verbose_name


class TableLablesManager(models.Manager):
    '''label表管理器'''
    def get_label_by_id(self,table_id=int):
        labels = self.filter(table_id=table_id)
        return labels
        
class TableLables(models.Model):
    '''给表打label'''
    #table_id = models.ForeignKey(Tables, verbose_name='tableid', on_delete=models.CASCADE)
    table_id = models.OneToOneField(Tables, verbose_name='tableid', on_delete=models.CASCADE)
    labels = models.CharField(default=None, max_length=100, null=True, verbose_name='表的自定义label，以英文|分割')
    
    objects = TableLablesManager()
    
    def __str__(self):
        return str(self.table_id)
    
    class Meta:
        db_table = 's_table_lable'
        verbose_name = '表的业务类型'
        verbose_name_plural = verbose_name


class TableCollection(models.Manager):
    
    def get_table_by_user(self, username=str):
        lable_dict = {}
        for i in range(1,5):
            lable_dict['lable' + str(i)] = self.filter(user=username,model_label=i).values('for_model','table_id','table_name')
                   
        return lable_dict
    
class TableCollection(models.Model):
    '''用户自定义收藏表'''
    lable = {1:1, 2:2, 3:3, 4:4}
    lable_status = ((k,v) for (k,v) in lable.items())
    
    table_id = models.ForeignKey(Tables, verbose_name='tableid', on_delete=models.CASCADE)
    table_name =models.CharField(default=None, max_length=100, verbose_name='表名')
    user = models.CharField(default=None, max_length=15,verbose_name='归属用户')
    model_label = models.SmallIntegerField(default=1, choices= lable_status, verbose_name='自定义块序号')
    for_model = models.CharField(default=None, max_length=20,verbose_name='类别')
    
    objects = TableCollection()
    
    def __str__(self):
        return(str(self.table_id_id)+ ':' + self.table_name)
        
    class Meta:
        db_table = 's_collection'
        verbose_name = '用户收藏表'
        verbose_name_plural = verbose_name       
        


    
       
        
    
    


    
    
    