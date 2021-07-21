from rest_framework import serializers
from .models import Deals, Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username', 'spent_money')

class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deals
        fields = ('customer', 'item', 'total', 'quantity', 'date' )