from rest_framework import serializers
from .models import CustomerAuthorization

class CustomerAuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAuthorization
        fields = '__all__'