# Generated by Django 2.2.3 on 2019-08-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPlus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_id', models.IntegerField(verbose_name='主表id')),
                ('table_name', models.CharField(default=None, max_length=30, verbose_name='表名')),
                ('user', models.CharField(default=None, max_length=20, verbose_name='用户')),
                ('create_time', models.CharField(default=None, max_length=20, verbose_name='时间')),
                ('comment', models.CharField(default=None, max_length=600, verbose_name='内容')),
            ],
            options={
                'verbose_name': '评论内容',
                'verbose_name_plural': '评论内容',
                'db_table': 's_comment_plus',
            },
        ),
    ]
