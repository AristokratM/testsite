from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Наиминование категории")

    def get_absolute_url(self):
        return reverse('category', kwargs={"pk": self.pk})


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="Наиминование")
    content = models.TextField(blank=True, max_length=5000, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обноволено")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-created_at']

