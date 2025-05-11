import os, base64
from django.conf import settings
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerPayment
from .serializers import CustomerPaymentSerializer

@api_view(['POST'])
def register_payment(request):
    try:
        data = request.data
        file = request.FILES['file']
        file_name = data['fileName']
        customerID = data['customerID']
        folder_path = os.path.join(settings.CUSTOMER_PAYMENT_FILES_DIR, customerID)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)

        # Serializar solo datos válidos
        data_dict = {
            'customerID': data['customerID'],
            'cotizacionID': data.get('cotizacionID'),
            'paymentDate': data['paymentDate'],
            'amount': data['amount'],
            'paymentType': data.get('paymentType'),
            'operationNumber': data.get('operationNumber'),
            'fileName': file_name,
            'observaciones': data.get('observaciones'),
            'status': data.get('status', False),
            'created_by': data.get('created_by'),
        }

        serializer = CustomerPaymentSerializer(data=data_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_payment_file_base64(request):
    try:
        paymentID = request.data['paymentID']
        payment = CustomerPayment.objects.get(paymentID=paymentID)
        file_path = os.path.join(settings.CUSTOMER_PAYMENT_FILES_DIR, payment.customerID, payment.fileName)

        if not os.path.exists(file_path):
            return Response({'error': 'File not found'}, status=404)

        with open(file_path, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
        return Response({'base64': encoded}, status=200)

    except CustomerPayment.DoesNotExist:
        return Response({'error': 'Payment not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


@api_view(['POST'])
def update_payment(request):
    try:
        paymentID = request.data['paymentID']
        payment = CustomerPayment.objects.get(paymentID=paymentID)

        serializer = CustomerPaymentSerializer(payment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(updated_at=timezone.now())
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    except CustomerPayment.DoesNotExist:
        return Response({'error': 'Payment not found'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


@api_view(['GET'])
def get_payments_by_customer(request):
    customerID = request.GET.get('customerID')
    cotizacionID = request.GET.get('cotizacionID')

    if not customerID or not cotizacionID:
        return Response({'error': 'customerID y cotizacionID son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

    payments = CustomerPayment.objects.filter(customerID=customerID, cotizacionID=cotizacionID)
    serializer = CustomerPaymentSerializer(payments, many=True)
    return Response(serializer.data)
