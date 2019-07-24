# Generated by Django 2.1.2 on 2019-07-24 13:29

from django.db import migrations, models
import django.db.models.deletion
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
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('table_id', models.IntegerField(verbose_name='表id')),
                ('table_name', models.CharField(max_length=50, verbose_name='表名')),
                ('db_name', models.CharField(max_length=10, verbose_name='表的库名')),
                ('table_subtype', models.CharField(choices=[('rn', '埋点数据'), ('order', '订单数据'), ('report', '报表数据'), ('other', '用户及设备属性及其他')], default='other', max_length=10, verbose_name='表业务子类型')),
                ('table_type', models.CharField(default='other', max_length=10, verbose_name='表业务类型')),
                ('db_type', models.CharField(choices=[('mysql', 'Mysql数据库'), ('hive', 'Hive数据库'), ('otherdb', '其他数据库')], default='other', max_length=10, verbose_name='数据库类型')),
                ('desc', models.CharField(max_length=128, verbose_name='表的简介')),
                ('detail', tinymce.models.HTMLField(verbose_name='表的详情')),
                ('status', models.SmallIntegerField(choices=[(0, '下线'), (1, '正常'), (2, '其他异常')], default=1, verbose_name='表的状态')),
            ],
            options={
                'verbose_name': '常用表',
                'verbose_name_plural': '常用表',
                'db_table': 's_hot_tables',
            },
        ),
        migrations.CreateModel(
            name='TableDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('clo_id', models.SmallIntegerField(verbose_name='列id')),
                ('clo_name', models.CharField(max_length=20, verbose_name='列名')),
                ('field_type', models.CharField(max_length=10, verbose_name='字段类型')),
                ('level', models.SmallIntegerField(default=0, verbose_name='字段等级,默认0普通')),
                ('comment', models.CharField(max_length=128, verbose_name='表的简介')),
            ],
            options={
                'verbose_name': '子表详细信息',
                'verbose_name_plural': '子表详细信息',
                'db_table': 's_table_details',
            },
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('table_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='表id')),
                ('table_name', models.CharField(max_length=50, verbose_name='表名')),
                ('db_name', models.CharField(max_length=10, verbose_name='表的库名')),
                ('table_type', models.CharField(default='other', max_length=10, verbose_name='表业务类型')),
                ('db_type', models.CharField(choices=[('mysql', 'Mysql数据库'), ('hive', 'Hive数据库'), ('otherdb', '其他数据库')], default='other', max_length=10, verbose_name='数据库类型')),
                ('desc', models.CharField(max_length=128, verbose_name='表的简介')),
            ],
            options={
                'verbose_name': '表库',
                'verbose_name_plural': '表库',
                'db_table': 's_tables',
            },
        ),
        migrations.AddField(
            model_name='tabledetails',
            name='table_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Tables', verbose_name='tableid'),
        ),
    ]
