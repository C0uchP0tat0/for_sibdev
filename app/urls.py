from django.urls import path
from .views import api_deals, api_сustomer, сustomer #CustomerDetailView

app_name = 'app'
urlpatterns = [
    #path ('detail/<int:pk>/', CustomerDetailView.as_view(), name='detail'),
    path('сustomer/<int:customer_id>/', сustomer),
    path('api/сustomer/', api_сustomer),
    path('api/deals/', api_deals),
    #path('api/post_deals/', api_post_deals)
]
