# Generated by Django 3.2.4 on 2021-09-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210912_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='article',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(max_length=54),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='preview',
            field=models.TextField(max_length=254),
        ),
    ]
