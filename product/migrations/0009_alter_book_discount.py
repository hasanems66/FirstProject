# Generated by Django 4.2.3 on 2023-08-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_rename_category_categorybook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='discount',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
