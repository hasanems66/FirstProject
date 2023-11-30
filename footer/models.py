from django.db import models

# Create your models here.



class Footer(models.Model):
    address = models.CharField(max_length=200, verbose_name= 'آدرس')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=12, verbose_name= 'تلفن')
    telegram = models.CharField(max_length=60, verbose_name= 'تلگرام')
    instagram = models.CharField(max_length=60, verbose_name= 'اینستاگرام')
    whatsapp = models.CharField(max_length=60, verbose_name= 'واتس آپ')
    twitter = models.CharField(max_length=60, verbose_name= 'توییتر')
    linkedin = models.CharField(max_length=60, blank=True, null=True, verbose_name= 'لینکدین')

    class Meta:
        verbose_name = 'پاورقی'
        verbose_name_plural = 'پاورقی ها'
