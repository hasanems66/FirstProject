# Generated by Django 4.2.3 on 2023-10-01 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_alter_categorycourse_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorycourse',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ایجاد'),
        ),
    ]
