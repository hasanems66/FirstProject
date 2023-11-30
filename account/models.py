from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.html import format_html


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email,and password.
        """
        if not phone:
            raise ValueError("Users must have an email address")

        user = self.model(
            phone=phone,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            phone,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="ایمیل",
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    fullname = models.CharField(max_length=50, verbose_name= 'نام و نام خانوادگی')
    image = models.ImageField(upload_to='profile/images', blank=True, null=True, verbose_name= 'عکس ')
    phone = models.CharField(max_length=12, unique=True, verbose_name= 'شماره تلفن' )
    is_active = models.BooleanField(default=True, verbose_name= 'فعال')
    is_admin = models.BooleanField(default=False, verbose_name= 'ادمین')

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="40px" height="30px"  alt="">')
        return format_html('<h4 style="color: red">تصویر ندارد</h4>')
    show_image.short_description = 'نمایش تصویر'

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'


class Otp(models.Model):
    phone = models.CharField(max_length=11, verbose_name= 'تلفن')
    token = models.CharField(max_length=200, null=True, verbose_name= 'توکن')
    code = models.SmallIntegerField( verbose_name= 'کد تایید')
    expiration_date = models.DateTimeField(auto_now_add=True, verbose_name= 'تاریخ انقضا')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'کد تایید'
        verbose_name_plural = 'کدهای تایید'





class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name= 'کاربر')
    fullname = models.CharField(max_length=40,verbose_name= 'نام و نام خانوارگی')
    phone = models.CharField(max_length=12, verbose_name= 'تلفن')
    email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    address = models.CharField(max_length=300, verbose_name= 'آدرس')
    postal_code = models.CharField(max_length=20, verbose_name= 'کد پستی')


    def __str__(self):
        return f'{self.user.fullname}-{self.address[:30]}'

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'



class Message(models.Model):
    full_name= models.CharField(max_length=30,verbose_name= 'نام و نام خانوارگی')
    email= models.EmailField(verbose_name= 'ایمیل')
    sub= models.CharField(max_length=30,verbose_name= 'موضوع')
    body= models.TextField(verbose_name= 'متن پیام')

    def __str__(self):
        return f'{self.full_name} - {self.body[:20]}'

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
#     fullname = models.CharField(max_length=30)