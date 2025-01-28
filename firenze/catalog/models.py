from django.db import models
from django.utils.html import format_html
from main.models import Shops
class Collections(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")
    external_code = models.CharField(max_length=127, verbose_name="Внешний код", default="")
    photo = models.ImageField(upload_to ='uploads/catalog/', verbose_name="Фотография", null=True, blank=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")
    external_code = models.CharField(max_length=127, verbose_name="Внешний код", default="")
    def __str__(self):
        return self.name
class Product(models.Model):
    external_code = models.CharField(max_length=127, verbose_name="Внешний код", default="")
    name = models.CharField(max_length=127, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    show_on_main_page = models.BooleanField(verbose_name="Показывать на главной", default=False)
    big_image = models.BooleanField(verbose_name="Большая картинка", null=True, blank=True)
    photo = models.ImageField(upload_to ='uploads/catalog/', verbose_name="Фотография", null=True, blank=True)
    collection = models.ForeignKey(Collections, on_delete=models.CASCADE, verbose_name="Коллекция", null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа", null=True)
    price = models.IntegerField(verbose_name="Цена", default=0)
    def __str__(self):
        return self.name
    
class Color(models.Model):
    external_code = models.CharField(max_length=127, verbose_name="Внешний код", default="")
    name = models.CharField(max_length=127, verbose_name="Название")
    color_code = models.CharField(max_length=63, verbose_name="HEX код цвета")

    def __str__(self):
        return self.name

class Material(models.Model):
    external_code = models.CharField(max_length=127, verbose_name="Внешний код", default="")
    name = models.CharField(max_length=127, verbose_name="Название")

    def __str__(self):
        return self.name

class Size(models.Model):
    external_code = models.CharField(max_length=127, verbose_name="Внешний код", default="")
    name = models.CharField(max_length=127, verbose_name="Название")
    sizeit = models.CharField(max_length=127, verbose_name="Размер ", default="", null=True, blank=True)
    sizeru = models.CharField(max_length=127, verbose_name="Размер ru", default="", null=True, blank=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    external_code = models.CharField(max_length=127, verbose_name="Внешний код", default="")
    name = models.CharField(max_length=127, verbose_name="Название")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Основной товар")
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(verbose_name="Цена")
    photo = models.ImageField(upload_to ='uploads/catalog/', verbose_name=" Фотография", null=True, blank=True)

    def list_image_tag(self):
        return format_html('<img style="max-width: 50px; " src="{}" />'.format(self.photo.url))
    list_image_tag.short_description = 'Просмотр'

    def __str__(self):
        return f"{self.name} - {self.size} - {self.color} - {self.material}"

class ProductTypeShopLeft(models.Model):
    external_code = models.CharField(max_length=127, verbose_name="Внешний код", default="")
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name="Товар")
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, verbose_name="Магазин")
    left = models.IntegerField(verbose_name="Остаток", default=0)
    
    def __str__(self):
        return f"{self.producttype} - {self.shop} - {self.left}"

class ProductTypePhotos(models.Model):
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to ='uploads/catalog/', verbose_name="Фотография")    