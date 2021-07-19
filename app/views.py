#import django_filters.rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import exception_handler
from rest_framework import status, generics
from django.http import HttpResponse
import csv
from .models import Deals, Customer
from .serializers import DealsSerializer, CustomerSerializer


@api_view(['GET'])
def api_сustomer(request):
    if request.method == 'GET':
        сustomer = Customer.objects.all()
        serializer = CustomerSerializer(сustomer, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def api_deals(request):
    if request.method == 'GET':
        deals = Deals.objects.all()
        serializer = DealsSerializer(deals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        with open("deals1.csv") as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                for row in file_reader:
                    created_cust = Customer.objects.update_or_create(
                        username=row[0])
                    user = Customer.objects.get(username = row[0])
                    created = Deals.objects.create(
                        customer=user,
                        item=row[1],
                        total=row[2],
                        quantity=row[3],
                        date=row[4])
        serializer = DealsSerializer(data=created)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
            
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)

