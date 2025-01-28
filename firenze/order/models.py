import datetime
from django.db import models
from personal.models import Customer
from main.models import Shops
from catalog.models import ProductType
class OrderTypes(models.TextChoices):
    delivery = "Доставка"
    pick_up = "Забрать из магазина"
class OrderStatus(models.TextChoices):
    waiting = "В обработке"
    payed = "Оплачен"
#Допилить 
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    date =  models.DateField(verbose_name="Дата заказа", blank=True, null=True, default=datetime.datetime.now)
    order_type = models.CharField(verbose_name="Тип заказа", choices=OrderTypes.choices, max_length=127, default=OrderTypes.pick_up)
    order_status = models.CharField(verbose_name="Статус заказа", choices=OrderStatus.choices, max_length=127, default=OrderStatus.waiting)
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, verbose_name="Магазин")
    name = models.CharField(verbose_name="Имя", max_length=127, blank=True, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=127, blank=True, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=63, blank=True, null=True)
    mail = models.CharField(verbose_name="Почта", max_length=127, blank=True, null=True)
    price = models.IntegerField(verbose_name="Цена", default=0)
    cart_items = models.ManyToManyField(ProductType)

    def __str__(self):
        return f"{self.date} {self.name} {self.last_name} {self.date}" 