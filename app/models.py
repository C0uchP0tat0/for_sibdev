from django.db import models
from django.utils import timezone

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

    def save(self, *args, **kwargs):
        total=0
        self.customer.spent_money = total+int(self.total)
        self.customer.save()
        super(Deals, self).save(*args, **kwargs)

class CustomerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('username')

class Customer(models.Model):
    username = models.TextField(max_length=30)
    spent_money = models.FloatField(null=True, blank=True)
    #gems = models.TextField(max_length=50)
    objects = CustomerManager()

    def __str__(self):
        return self.username

    
