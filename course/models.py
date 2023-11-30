from ckeditor.fields import RichTextField
from django.db import models
from django.utils.html import format_html

from account.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify



class CategoryCourse(models.Model):
    title = models.CharField(max_length=30, verbose_name='عنوان')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='courses', verbose_name='نویسنده')
    category = models.ManyToManyField(CategoryCourse, related_name='courses', verbose_name='دسته بندی')
    image = models.ImageField(upload_to='images/course',blank=True, null=True, verbose_name='تصویر دوره')
    # body = models.TextField(verbose_name='توضیحات')
    body = RichTextField(verbose_name='توضیحات')
    video_file = models.FileField(upload_to='deploy/videos', verbose_name='فایل ویدئویی')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='آپدیت')
    slug = models.SlugField(blank=True, unique=True,allow_unicode=True, verbose_name='اسلاگ')
    views = models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید')
    status = models.BooleanField(default=True, verbose_name='وضعیت')
    pub_date = models.DateField(default=timezone.now, verbose_name='زمان انتشار')



    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Course, self).save()

    def get_absolute_url(self):
        return reverse('course:course_details', args=[self.slug])

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="40px" height="30px"  alt="">')
        return format_html('<h4 style="color: red">تصویر ندارد</h4>')
    show_image.short_description = 'نمایش تصویر'


    def __str__(self):
        return f'{self.title} - {self.author.fullname}'


    class Meta:
        ordering= ('-pub_date',)
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'



class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments', verbose_name= 'دوره')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name= 'کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name= 'والد')
    body = models.TextField(verbose_name= 'متن پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= 'تاریخ ایجاد')


    def __str__(self):
        return self.body[:50 ]

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'





class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='likes', verbose_name='دوره')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')


    def __str__(self):
        return self.user.fullname


    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'

