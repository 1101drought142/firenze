import datetime
from django.db import models

class News(models.Model):
    name = models.CharField(verbose_name="Название", max_length=127)
    slug = models.CharField(verbose_name="Слаг", max_length=127)
    
    date = models.DateField(verbose_name="Дата", default=datetime.datetime.now)
    photo = models.ImageField(upload_to ='uploads/news/', verbose_name="Фотография") 

    first_description = models.TextField(verbose_name="Описание до фото", null=True, blank=True)
    second_description = models.TextField(verbose_name="Описание после фото", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    

class NewsPhotos(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to ='uploads/news/', verbose_name="Фотография") 

class ShopTypes(models.TextChoices):
    tc = "Торговые центры"
    autlet = "Аутлеты"
    corner = "Корнеры"

class Shops(models.Model):
    name = models.CharField(verbose_name="Название", max_length=127)
    address = models.CharField(verbose_name="Адрес", max_length=255, null=True, blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=127, null=True, blank=True)
    photo = models.ImageField(upload_to ='uploads/shop/', verbose_name="Фотография", null=True, blank=True) 
    shop_type = models.CharField(verbose_name="Тип магазина", choices=ShopTypes.choices, max_length=127, null=True, blank=True)
    external_code = models.CharField(max_length=127, verbose_name="Внешний код", default="")

    def __str__(self):
        return f"{self.name}"
    