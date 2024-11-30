from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    show_on_main_page = models.BooleanField(verbose_name="Показывать на главной", default=False)
    big_image = models.BooleanField(verbose_name="Большая картинка", default=False)
    photo = models.ImageField(upload_to ='uploads/catalog/% Y/% m/% d/', verbose_name="Фотография")

    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")
    color_code = models.CharField(max_length=63, verbose_name="HEX код цвета")

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=127, verbose_name="Название")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Основной товар")
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(verbose_name="Цена")
    photo = models.ImageField(upload_to ='uploads/catalog/% Y/% m/% d/', verbose_name=" Фотография")
    left = models.IntegerField(verbose_name="Остаток", default=0)

    def __str__(self):
        return f"{self.name} - {self.size} - {self.color} - {self.material} - {self.left}"

class ProductTypePhotos(models.Model):
    producttype = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to ='uploads/catalog/% Y/% m/% d/', verbose_name="Фотография")    