# Generated by Django 2.1.3 on 2018-12-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexPage', '0002_auto_20181226_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='is_timeout',
            field=models.BooleanField(default=False, verbose_name='工作是否过期'),
        ),
        migrations.AddField(
            model_name='work',
            name='topic',
            field=models.TextField(default='工作详情', verbose_name='班级工作内容'),
        ),
    ]
