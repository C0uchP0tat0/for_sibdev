from django.urls import path
from .views import api_deals, api_сustomer

app_name = 'app'
urlpatterns = [
    path('api/сustomer/', api_сustomer),
    path('api/deals/', api_deals),
    #path('api/post_deals/', api_post_deals)
]
