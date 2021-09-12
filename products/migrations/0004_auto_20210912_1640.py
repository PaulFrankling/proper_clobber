# Generated by Django 3.2.4 on 2021-09-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210723_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, default='', max_length=254),
        ),
    ]
