from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ListOfItemValue
from .serializers import ListOfItemValueSerializer

class ListItemsByListID(APIView):
    def get(self, request, list_id):
        items = ListOfItemValue.objects.filter(listID=list_id)
        serializer = ListOfItemValueSerializer(items, many=True)
        return Response(serializer.data)
