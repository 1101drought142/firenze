from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=63, blank=True, null=True)
    photo = models.ImageField(upload_to ='uploads/customer/', verbose_name="Фотография", blank=True, null=True) 
    cart = models.JSONField(verbose_name="Корзина", null=True, blank=True)
    favourites = models.JSONField(verbose_name="Избранное", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customer.save()