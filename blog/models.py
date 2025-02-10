from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, default='', null=False, verbose_name='آدرس دسته‌بندی', unique=True)
    status = models.BooleanField(default=True, verbose_name='ایا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی ها'
        ordering = ['position']

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', 'منتشر شده')
    )
    title = models.CharField(max_length=200, db_index=True, verbose_name='عنوان')
    author = models.CharField(max_length=100, verbose_name='نویسنده', null=True)
    slug = models.SlugField(max_length=100, default='', null=False, db_index=True, unique=True, verbose_name='عنوان در url')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته‌بندی')
    content = models.TextField(verbose_name='متن اصلی', db_index=True,)
    thumbnail = models.ImageField(upload_to='images', verbose_name='تصویر مقاله', null=True)
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ نگارش')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    author = models.CharField(max_length=100, db_index=True, verbose_name='نویسنده')
    content = models.TextField(verbose_name='محتوا', db_index=True,)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ نگارش')
    is_approve = models.BooleanField(default=False, verbose_name='تایید شده / نشده')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'{self.article}'
