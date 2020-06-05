# Generated by Django 2.2.3 on 2019-08-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_tablecollection_model_label'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tablecollection',
            options={'verbose_name': '用户收藏表', 'verbose_name_plural': '用户收藏表'},
        ),
        migrations.AlterField(
            model_name='tablecollection',
            name='for_model',
            field=models.CharField(default=None, max_length=20, verbose_name='类别'),
        ),
        migrations.AlterModelTable(
            name='tablecollection',
            table='s_collection',
        ),
    ]