# Generated by Django 4.2.3 on 2023-08-29 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_information_book_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0006_alter_discountcode_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='discount',
            field=models.SmallIntegerField(default=0, verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='name',
            field=models.CharField(max_length=12, unique=True, verbose_name='نام کد تخفیف'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='quantity',
            field=models.SmallIntegerField(default=1, verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='پرداخت شده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0, verbose_name='قیمت کل'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.book', verbose_name='کتاب'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.order', verbose_name='سفارش'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.PositiveIntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.SmallIntegerField(verbose_name='تعداد'),
        ),
    ]
