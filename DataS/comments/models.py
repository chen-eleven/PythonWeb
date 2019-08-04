from django.db import models
# Create your models here.


class CommentPlusManager(models.Manager):
    '''评论管理器'''
    def add_one_comm(self, table_id, table_name, user, create_time, comment ):
        try:
            self.create(table_id=table_id, table_name=table_name, 
                                   user=user, create_time=create_time, 
                                   comment=comment)
        except Exception as e:
            print('e: ', e)
        # 3.返回passport
        return ('insert sucessfly')
    
    def get_comm_by_id(self, table_id=int):
        comment_plus_li = self.filter(table_id=table_id).order_by('create_time')
        return comment_plus_li
    
class CommentPlus(models.Model):
    '''评论'''
    table_id = models.IntegerField(verbose_name='主表id')
    table_name = models.CharField(default=None, max_length=30, verbose_name='表名')
    user = models.CharField(default=None, max_length=20, verbose_name='用户')
    create_time = models.CharField(default=None, max_length=20, verbose_name='时间')
    comment = models.CharField(default=None, max_length=600, verbose_name='内容')
    
    objects = CommentPlusManager()
    
    def __str__(self):
        return self.table_name
    
    class Meta:
        db_table = 's_comment_plus'
        verbose_name = '评论内容'
        verbose_name_plural = verbose_name
    
    