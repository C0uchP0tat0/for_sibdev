from django.urls import path
from .views import api_deals, api_сustomer, сustomer

app_name = 'app'
urlpatterns = [
    path('сustomer/<int:customer_id>/', сustomer),
    path('api/сustomer/', api_сustomer),
    path('api/deals/', api_deals),
]
