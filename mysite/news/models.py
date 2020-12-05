from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
