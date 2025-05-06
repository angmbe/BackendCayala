# views.py
import bcrypt
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Profile

class RegisterUserView(APIView):
    def post(self, request):
        data = request.data
        password = data.get("password")
        if not password:
            return Response({"error": "Password is required"}, status=400)

        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            user = User.objects.create(
                username=data["username"],
                password_hash=hashed.decode('utf-8'),
                fullname=data["fullname"],
                profile_id=data["profile_id"],
                customer_id=data.get("customer_id"),
                status=True,
                created_by=1,
                created_at=timezone.now()
            )
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class LoginUserView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.select_related('profile').get(username=username)
        except User.DoesNotExist:
            return Response({"error": "Invalid username or password"}, status=400)

        if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
            return Response({
                "fullname": user.fullname,
                "profileID": user.profile.profileid,
                "profileName": user.profile.profilename,
                "id" : user.customer.id,
                "type" : user.customer.type
            })
        else:
            return Response({"error": "Invalid username or password"}, status=400)