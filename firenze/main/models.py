import datetime
from django.db import models

class News(models.Model):
    name = models.CharField(verbose_name="Название", max_length=127)
    date = models.DateField(verbose_name="Дата", default=datetime.datetime.now)
    photo = models.ImageField(upload_to ='uploads/news/% Y/% m/% d/', verbose_name="Фотография") 

    first_description = models.TextField(verbose_name="Описание до фото", null=True, blank=True)
    second_description = models.TextField(verbose_name="Описание после фото", null=True, blank=True)

class NewsPhotos(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to ='uploads/news/% Y/% m/% d/', verbose_name="Фотография") 
