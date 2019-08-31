from django.db import models
from db.base_model import BaseModel
from utils.get_hash import get_hash

class PassportManager(models.Manager):
    def add_one_passport(self, username, password, email):
        '''添加一个账户信息'''
        try:
            passport = self.create(username=username, password=get_hash(password), email=email)
        except Exception as e:
            print('e: ', e)
        # 3.返回passport
        return passport

    def get_one_passport(self, username, password):
        '''根据用户名密码查找账户的信息'''
        try:
            passport = self.get(username=username, password=get_hash(password))
        except self.model.DoesNotExist:
            # 账户不存在
            passport = None
        return passport

    def check_passport(self, username):
        try:
            passport = self.get(username=username)
        except self.model.DoesNotExist:
            passport = None
        if passport:
            return True
        return False
    
    def get_info(self, uid):
        userinfo = self.filter(id=uid)
        return userinfo
# Create your models here.
class Passport(BaseModel):
    '''用户模型类'''
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名称')
    password = models.CharField(max_length=40, verbose_name='用户密码')
    email = models.EmailField(verbose_name='用户邮箱')
    is_active = models.BooleanField(default=False, verbose_name='激活状态')

    # 用户表的管理器
    objects = PassportManager()

    class Meta:
        db_table = 's_user_account'
        
        
        