from django.shortcuts import render
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import exception_handler
from rest_framework import status, generics
from django.http import HttpResponse
import csv
from .models import Deals, Customer
from .serializers import DealsSerializer, CustomerSerializer

def сustomer(request, customer_id):
    deals = Deals.objects.filter(customer=customer_id)
    customers = Customer.objects.all()
    current_customer = Customer.objects.get(pk=customer_id)
    spent_money = deals.aggregate(total_spent_money=Sum('total'))
    context = {'deals': deals,'customers': customers,
               'spent_money': spent_money, 'current_customer': current_customer}
    return render(request, 'сustomer.html', context)

@api_view(['GET'])
def api_сustomer(request):
    if request.method == 'GET':
        сustomer = Customer.objects.all()[0:5]
        serializer = CustomerSerializer(сustomer, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def api_deals(request):
    if request.method == 'GET':
        deals = Deals.objects.all()
        serializer = DealsSerializer(deals, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        with open("deals.csv") as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for row in file_reader:
                    created_cust = Customer.objects.update_or_create(
                        username=row[0],
                        defaults={'spent_money': 0})
                    user = Customer.objects.get(username=row[0])
                    created = Deals.objects.update_or_create(
                        customer=user,
                        item=row[1],
                        total=row[2],
                        quantity=row[3],
                        date=row[4])
        user_iter = Customer.objects.all()
        for u in user_iter:
            deal = Deals.objects.filter(customer=u)
            gem_list=[]
            gem_list.append(deal)
            gem_str=str(gem_list)
            symbols = ['[<QuerySet ','[<Deals: ','>','<Deals: ','>]>]']
            gem_str_remove=gem_str.replace('[<QuerySet ', '').replace(
                '[<Deals: ', '').replace('>', '').replace(
                '<Deals: ', '').replace(']', '').replace("'...(remaining elements truncated)...'", "")        
            spent_money = deal.aggregate(total_spent_money=Sum('total'))
            Customer.objects.filter(username=u.username).update(
                                    spent_money=spent_money['total_spent_money'],
                                    gems = gem_str_remove)
        serializer = DealsSerializer(data=created)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
            
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)

