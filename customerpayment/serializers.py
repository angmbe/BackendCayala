from rest_framework import serializers
from .models import CustomerPayment

class CustomerPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPayment
        fields = '__all__'