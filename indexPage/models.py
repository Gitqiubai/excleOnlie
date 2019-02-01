from django.db import models

# Create your models here.




class work(models.Model):

    work_name = models.CharField(max_length=255,verbose_name='工作名称')
    creator = models.CharField(max_length=100,default='admin',verbose_name='创建者')
    topic = models.TextField(default='工作详情',verbose_name='班级工作内容')
    is_timeout = models.BooleanField(default=False,verbose_name='工作是否过期')
    work_create_date = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')


    class Meta:

        verbose_name = '工作'
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.work_name


class workData(models.Model):

    student_number = models.CharField(max_length=10,verbose_name='学号')
    work_id = models.CharField(max_length=10,verbose_name='工作id')
    work_content = models.TextField(verbose_name='内容')
    date = models.DateTimeField(auto_now_add=True,verbose_name='提交时间')

    class Meta:

        verbose_name = '用户提交数据表'
        verbose_name_plural = verbose_name


    def __str__(self):

        return self.student_number
