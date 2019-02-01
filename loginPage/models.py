from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class userTable(AbstractUser):
    nickName = models.CharField(max_length=20,default='未命名',verbose_name='姓名')

    class Meta:

        verbose_name = '用户数据'
        verbose_name_plural = verbose_name


    def __str__(self):

        return self.username
