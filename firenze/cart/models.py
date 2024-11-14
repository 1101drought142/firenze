from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

class Color(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")
    color_code = models.CharField(max_length=63, verbose_name="HEX код цвета")

class Material(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")

class Size(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")

class ProductType(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, blank=True)

class ProductTypePhotos(models.Model):
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to ='uploads/% Y/% m/% d/', verbose_name="Фотография")