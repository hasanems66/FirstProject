# Generated by Django 4.2.3 on 2023-09-02 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_article_author_alter_article_body_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article_comment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
    ]
