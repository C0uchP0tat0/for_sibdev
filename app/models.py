from django.db import models
from django.utils import timezone

class Customer(models.Model):
    username = models.TextField(max_length=30)
    spent_money = models.FloatField(null=True, blank=True)
    gems = models.TextField(max_length=50)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        list_spent_money=[]
        s = 0
        list_spent_money.append(self.spent_money)
        for m in list_spent_money:
            s+=int(m)
            self.spent_money = s
            super(Customer, self).save(*args, **kwargs)

class Deals(models.Model):
    customer = models.TextField(max_length=30)
    item = models.TextField(max_length=50)
    total = models.FloatField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
        
    def __str__(self):
        return self.customer


