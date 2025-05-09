from rest_framework import serializers
from .models import ListOfItemValue

class ListOfItemValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfItemValue
        fields = ['valueID', 'descriptionValue','icon']
