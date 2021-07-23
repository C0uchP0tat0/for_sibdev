from django.db import models
from django.utils import timezone
from django.db.models import Sum

class DealsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('customer')

class Deals(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    item = models.TextField(max_length=50)
    total = models.FloatField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    objects = DealsManager()
            
    def __str__(self):
        return self.item

class CustomerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-spent_money')

class Customer(models.Model):
    username = models.TextField(max_length=30)
    spent_money = models.FloatField(null=True, blank=True)
    #gems = models.TextField()
    objects = CustomerManager()

    def __str__(self):
        return self.username