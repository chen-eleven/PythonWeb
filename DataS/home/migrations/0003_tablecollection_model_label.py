# Generated by Django 2.2.3 on 2019-08-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tablecollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablecollection',
            name='model_label',
            field=models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1, verbose_name='自定义块序号'),
        ),
    ]
