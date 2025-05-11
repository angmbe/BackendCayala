import base64, os
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerLegal
from .serializers import CustomerLegalSerializer
from django.utils import timezone

@api_view(['POST'])
def upload_document(request):
    try:
        customerID = request.data['customerID']
        documentID = request.data['documentID']
        expiredDate = request.data['expiredDate']
        file = request.FILES['file']
        created_by = request.data.get('created_by', 0)

        #file_name = f"{documentID}_{file.name}"
        file_name = request.data['fileName']
        customer_folder = os.path.join(settings.CUSTOMER_FILES_DIR, customerID)
        os.makedirs(customer_folder, exist_ok=True)
        file_path = os.path.join(customer_folder, file_name)

        with open(file_path, 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)

        record = CustomerLegal.objects.create(
            customerID=customerID,
            documentID=documentID,
            expiredDate=expiredDate,
            fileName=file_name,
            status=False,
            created_by=created_by,
        )

        return Response(CustomerLegalSerializer(record).data, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_document_base64(request):
    try:
        customerID = request.data['customerID']
        documentID = request.data['documentID']

        record = CustomerLegal.objects.get(customerID=customerID, documentID=documentID)
        customer_folder = os.path.join(settings.CUSTOMER_FILES_DIR, customerID)
        file_path = os.path.join(customer_folder, record.fileName)

        if not os.path.exists(file_path):
            return Response({'error': 'File not found'}, status=404)

        with open(file_path, 'rb') as file:
            encoded = base64.b64encode(file.read()).decode('utf-8')

        return Response({'base64': encoded}, status=200)

    except CustomerLegal.DoesNotExist:
        return Response({'error': 'Document not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
def approved_document(request):
    print("✅ Entró al método approved_document")
    try:
        legalID = request.data['legalID']

        if not legalID:
            return Response({'error': 'legalID es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            document = CustomerLegal.objects.get(legalID=legalID)
        except CustomerLegal.DoesNotExist:
            return Response({'error': 'Documento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        document.status = True
        document.updated_at = timezone.now()
        document.save()

        return Response({'message': 'Documento actualizado correctamente'}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_documents_by_customer(request, customerID):
    try:
        records = CustomerLegal.objects.filter(customerID=customerID)
        serializer = CustomerLegalSerializer(records, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['POST'])
def test_post(request):
    print("✅ Entró al método test_post")
    return Response({"message": "POST recibido correctamente"})


