# Generated by Django 2.1.2 on 2019-07-21 06:49

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotTables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('table_id', models.IntegerField(verbose_name='表id')),
                ('table_name', models.CharField(max_length=50, verbose_name='表名')),
                ('db_name', models.CharField(max_length=10, verbose_name='表的库名')),
                ('table_subtype', models.CharField(choices=[('rn', '埋点数据'), ('order', '订单数据'), ('report', '报表数据'), ('other', '用户及设备属性及其他')], default='other', max_length=10, verbose_name='表业务子类型')),
                ('table_type', models.CharField(default='other', max_length=10, verbose_name='表业务类型')),
                ('db_type', models.CharField(default='other', max_length=10, verbose_name='数据库类型')),
                ('desc', models.CharField(max_length=128, verbose_name='表的简介')),
                ('detail', tinymce.models.HTMLField(verbose_name='表的详情')),
                ('status', models.SmallIntegerField(choices=[(0, '下线'), (1, '正常'), (2, '其他异常')], default=1, verbose_name='表的状态')),
            ],
            options={
                'verbose_name': '常用表',
                'verbose_name_plural': '常用表',
                'db_table': 's_tables',
            },
        ),
    ]
