from django.urls import path
from .views import api_deals, api_сustomer, сustomer

app_name = 'app'
urlpatterns = [
    path('сustomer/', сustomer, name='spent_money'),
    path('api/сustomer/', api_сustomer),
    path('api/deals/', api_deals),
    #path('api/post_deals/', api_post_deals)
]
