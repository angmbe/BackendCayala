# customerprice/urls.py
from django.urls import path
from .views import CustomerPriceByCustomerView

urlpatterns = [
    path('customer-price/<str:customer>/', CustomerPriceByCustomerView.as_view(), name='customer-price-by-id'),
]
