# Generated by Django 2.2.3 on 2019-08-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
    ]
