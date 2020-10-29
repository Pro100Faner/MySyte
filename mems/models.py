from django.db import models
from django.shortcuts import reverse

# Create your models here.


class MemPost(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название mem')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Ссылка на mem')
    body = models.TextField(blank=True, db_index=True, verbose_name='Текст')
    date_pub = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    image = models.ImageField(null=True, upload_to="images/", verbose_name="Изображение")

    def get_absolute_url(self):
        return reverse('mem_detail_url', kwargs={'slug': self.slug})


    def __str__(self):
        return '{}'.format(self.title)