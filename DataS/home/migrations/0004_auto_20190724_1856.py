# Generated by Django 2.2.3 on 2019-07-24 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190724_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabledetails',
            name='table_id',
            field=models.IntegerField(verbose_name='tableid'),
        ),
    ]
