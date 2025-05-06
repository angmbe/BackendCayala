from rest_framework import serializers
from .models import CustomerLegal

class CustomerLegalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLegal
        fields = '__all__'