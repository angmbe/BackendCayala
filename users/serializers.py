# users/serializers.py
from rest_framework import serializers
from .models import Users, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profileID', 'profileName']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(source='profileID', read_only=True)

    class Meta:
        model = Users
        fields = ['userID', 'userName', 'fullName', 'status', 'profileID', 'profile']
