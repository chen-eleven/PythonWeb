from django.db import models
from db.base_model import BaseModel
from users.models import Passport
from home.models import Tables
# Create your models here.
class Comments(BaseModel):
    disabled = models.BooleanField(default=False, verbose_name="禁用评论")
    user = models.ForeignKey('users.Passport', verbose_name="用户ID", on_delete=models.CASCADE)
    book = models.ForeignKey('home.Tables', verbose_name="tableID", on_delete=models.CASCADE)
    content = models.CharField(max_length=1000, verbose_name="评论内容")
    title = models.CharField(max_length=20, verbose_name="评论标题", default="")
    class Meta:
        db_table = 's_comment_table'
