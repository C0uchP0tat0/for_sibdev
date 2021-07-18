from django.db import models
from django.utils import timezone

class CalcManager(models.Manager):
    def get_query_set(self):
        spent_money=super(CalcManager, self).get_query_set().extra(select={'spent_money': "first+second"})

class Customer(models.Model):
    #username = models.TextField(max_length=30)
    first = models.FloatField(null=True)
    second = models.FloatField(null=True)
    spent_money = models.FloatField(null=True, blank=True)
    objects = CalcManager()
    #gems = models.TextField(max_length=50)

class DealsQuerySet(models.QuerySet):
    def order_by_customer_count(self):
        return self.annotate(cnt=models.Count('deals.customer')).order_by('cnt')

class DealsManager(models.Manager):
    def get_queryset(self):
        return DealsQuerySet(self.model, using=self._db)

    def order_by_customer_count(self):
        return self.get_queryset().order_by_customer_count()

class Deals(models.Model):
    customer = models.TextField(max_length=30)
    item = models.TextField(max_length=50)
    total = models.FloatField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    objects = DealsManager()
    
    def __str__(self):
        return self.customer
