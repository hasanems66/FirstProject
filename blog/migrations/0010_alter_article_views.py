# Generated by Django 4.2.3 on 2023-10-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_article_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='تعداد بازدید'),
        ),
    ]