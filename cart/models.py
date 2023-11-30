from django.db import models

from account.models import User
from product.models import Book


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name= 'کاربر')
    total_price = models.IntegerField(default=0, verbose_name= 'قیمت کل')
    address = models.TextField(blank=True, null=True, verbose_name= 'آدرس')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= 'تاریخ ایجاد')
    is_paid = models.BooleanField(default=False, verbose_name= 'پرداخت شده')


    def __str__(self):
        return self.user.fullname

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name= 'سفارش')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='items', verbose_name= 'کتاب')
    quantity = models.SmallIntegerField(verbose_name= 'تعداد')
    price = models.PositiveIntegerField(verbose_name= 'قیمت')

    class Meta:
        verbose_name = 'آیتم مربوط به سفارش'
        verbose_name_plural = 'آیتم های مربوط به سفارشات'


class DiscountCode(models.Model):
    name = models.CharField(max_length=12, unique=True, verbose_name= 'نام کد تخفیف')
    discount = models.SmallIntegerField(default=0, verbose_name= 'درصد تخفیف')
    quantity = models.SmallIntegerField(default=1, verbose_name= 'تعداد')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کدهای تخفیف'
