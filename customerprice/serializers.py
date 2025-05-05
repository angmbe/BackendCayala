# customerprice/serializers.py
from rest_framework import serializers
from .models import VwCustomerPrice

class VwCustomerPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VwCustomerPrice
        fields = '__all__'
