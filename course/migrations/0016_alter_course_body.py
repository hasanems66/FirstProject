# Generated by Django 4.2.3 on 2023-11-14 06:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_course_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات'),
        ),
    ]
