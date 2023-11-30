from math import ceil

from django.db import models
from django.utils.text import slugify
from django.urls import reverse



class CategoryBook(models.Model):
    title = models.CharField(max_length=20, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی کتاب'
        verbose_name_plural = 'دسته بندی کتابها'



class Author(models.Model):
    full_name = models.CharField(max_length=30, verbose_name='نام کامل')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسنده ها'



class PrintYear(models.Model):
    title = models.CharField(max_length=4, verbose_name= 'عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سال انتشار'
        verbose_name_plural = 'سال های انتشار'

class Publisher(models.Model):
    title = models.CharField(max_length=50, verbose_name= 'عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ناشر'
        verbose_name_plural = 'ناشرها'


class Subject(models.Model):
    title = models.CharField(max_length=20, verbose_name= 'عنوان')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'موضوع ها'



class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name= 'عنوان')
    author = models.ForeignKey(Author,null=True, on_delete=models.CASCADE, related_name='books', verbose_name= 'نویسنده')
    category = models.ManyToManyField(CategoryBook, related_name='books', verbose_name= 'دسته بندی')
    print_year = models.ForeignKey(PrintYear, on_delete=models.CASCADE, null=True, blank=True, related_name='books', verbose_name= 'سال انتشار')
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.CASCADE, verbose_name= 'ناشر')
    translator = models.CharField(max_length=50, null=True, verbose_name= 'مترجم')
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE, related_name='books', verbose_name= 'موضوع')
    price = models.IntegerField(verbose_name='قیمت')
    discount = models.SmallIntegerField(blank=True, null=True, verbose_name= 'کد تخفیف')
    discounted_price = models.SmallIntegerField(null=True, blank=True, verbose_name='قیمت تخفیف خورده')
    image = models.ImageField(upload_to='products', null=True, blank=True, verbose_name= 'عکس')
    slug = models.SlugField(blank=True,allow_unicode=True, verbose_name= 'اسلاگ')
    created_at = models.DateField(auto_now_add=True, verbose_name= 'تاریخ انتشار')


    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'


    def get_absolute_url(self):
        # return reverse('product:book_detail', args=[self.title])
        return reverse('product:book_detail', args=[self.slug])

    def discount_percentage(self):
        if self.discount:
            discount = self.discount
            multiplier = discount / 100.
            old_price = self.price
            new_price = ceil(old_price - (old_price * multiplier))
            self.discounted_price = new_price

    def save(self, force_insert=False, force_update=False, using=None, update_fields='discounted_price'):
        self.slug = slugify(self.title,allow_unicode=True)
        self.discount_percentage()
        super(Book, self).save()

    def __str__(self):
        return self.title



class Information(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='informations', verbose_name= 'کتاب')
    book_cover_type = models.CharField(max_length=50, verbose_name= 'نوع جلد کتاب')
    number_of_pages = models.IntegerField(null=True, blank=True, verbose_name= 'تعداد صفحات کتاب')
    weight = models.SmallIntegerField(verbose_name= 'وزن کتاب')
    international_code = models.CharField(max_length=13, verbose_name= 'کد شابک')

    def __str__(self):
        return f'{self.book}-{self.international_code}'

    class Meta:
        verbose_name = 'اطلاعات'
        verbose_name_plural = 'اطلاعات'




