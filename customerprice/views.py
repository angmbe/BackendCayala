# customerprice/views.py
from rest_framework import generics
from .models import VwCustomerPrice
from .serializers import VwCustomerPriceSerializer

class CustomerPriceByCustomerView(generics.ListAPIView):
    serializer_class = VwCustomerPriceSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer']
        return VwCustomerPrice.objects.filter(customer=customer_id)

