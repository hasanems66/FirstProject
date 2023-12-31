# Generated by Django 4.2.3 on 2023-08-29 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_book_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'نویسنده', 'verbose_name_plural': 'نویسنده ها'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('-created_at',), 'verbose_name': 'کتاب', 'verbose_name_plural': 'کتاب ها'},
        ),
        migrations.AlterModelOptions(
            name='categorybook',
            options={'verbose_name': 'دسته بندی کتاب', 'verbose_name_plural': 'دسته بندی کتابها'},
        ),
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name': 'اطلاعات', 'verbose_name_plural': 'اطلاعات'},
        ),
        migrations.AlterModelOptions(
            name='printyear',
            options={'verbose_name': 'سال انتشار', 'verbose_name_plural': 'سال های انتشار'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'ناشر', 'verbose_name_plural': 'ناشرها'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'موضوع', 'verbose_name_plural': 'موضوع ها'},
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=30, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='product.author', verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(related_name='books', to='product.categorybook', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='book',
            name='discount',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='کد تخفیف'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='book',
            name='print_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='product.printyear', verbose_name='سال انتشار'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.publisher', verbose_name='ناشر'),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='book',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='product.subject', verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.CharField(max_length=50, null=True, verbose_name='مترجم'),
        ),
        migrations.AlterField(
            model_name='categorybook',
            name='title',
            field=models.CharField(max_length=20, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='printyear',
            name='title',
            field=models.CharField(max_length=4, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='title',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=20, verbose_name='عنوان'),
        ),
    ]
