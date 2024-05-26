from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Purchase, Sale

# https://docs.djangoproject.com/en/4.2/topics/signals/

'''
@receiver(pre_save, sender=Purchase)
def calculate_total_price(sender, instance, **kwargs):
    # Toplam fiyat hesapla:
    instance.price_total = instance.quantity * instance.price


@receiver(pre_save, sender=Sale)
def calculate_total_price(sender, instance, **kwargs):
    # Toplam fiyat hesapla:
    instance.price_total = instance.quantity * instance.price
'''

@receiver(pre_save, sender=Purchase)
@receiver(pre_save, sender=Sale)
def calculate_total_price(sender, instance, **kwargs):
    # Toplam fiyat hesapla:
    instance.price_total = instance.quantity * instance.price
