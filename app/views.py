import django_filters.rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import exception_handler
from rest_framework import status, generics
from django.http import HttpResponse
import csv
from .models import Deals
from .serializers import DealsSerializer

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
                    created = Deals.objects.get_or_create(
                        customer=row[0],
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

