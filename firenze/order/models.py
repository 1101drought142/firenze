from django.db import models
from personal.models import Customer

class OrderTypes(models.TextChoices):
    delivery = "Доставка"
    pick_up = "Забрать из магазина"
#Допилить 
class Order(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    date =  models.DateField(verbose_name="Дата заказа", blank=True, null=True)
    order_type = models.CharField(verbose_name="Тип заказа", choices=OrderTypes.choices, max_length=127)
