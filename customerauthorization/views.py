import os
import base64
import datetime
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.timezone import now
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from xhtml2pdf import pisa
from .models import CustomerAuthorization
from .serializers import CustomerAuthorizationSerializer

#PDF_DIR = os.path.join(settings.MEDIA_ROOT, 'autorizaciones')
PDF_DIR = settings.CUSTOMER_AUTORIZACIONES_DIR
os.makedirs(PDF_DIR, exist_ok=True)

def generate_pdf_from_html(context, filename):
    html = render_to_string("autorizacion.html", context)
    filepath = os.path.join(PDF_DIR, filename)

    with open(filepath, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(html, dest=pdf_file)

    return filepath if not pisa_status.err else None

# @api_view(['POST'])
# def generar_autorizacion_pdf(request):
#     customerID = request.data.get('customerID')
#     cotizacionID = request.data.get('cotizacionID')
#     created_by = request.data.get('created_by', 0)

#     if not customerID or not cotizacionID:
#         return Response({'error': 'Faltan parámetros requeridos'}, status=status.HTTP_400_BAD_REQUEST)

#     timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
#     filename = f"Auth_{customerID}_{timestamp}.pdf"

#     context = {
#         'customerID': customerID,
#         'cotizacionID': cotizacionID,
#         'fecha': now().strftime('%d/%m/%Y %H:%M:%S')
#     }

#     pdf_path = generate_pdf_from_html(context, filename)
#     if not pdf_path:
#         return Response({'error': 'No se pudo generar el PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     with open(pdf_path, "rb") as pdf_file:
#         pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')

#     auth = CustomerAuthorization.objects.create(
#         customerID=customerID,
#         cotizacionID=cotizacionID,
#         fileName=filename,
#         created_by=created_by,
#         created_at=now()
#     )

#     return Response({
#         'fileName': filename,
#         'base64': pdf_base64
#     }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def generar_autorizacion_pdf(request):
    customerID = request.data.get('customerID')
    cotizacionID = request.data.get('cotizacionID')
    created_by = request.data.get('created_by', 0)

    if not customerID or not cotizacionID:
        return Response({'error': 'Faltan parámetros requeridos'}, status=status.HTTP_400_BAD_REQUEST)

    # Buscar si ya existe un registro
    existing = CustomerAuthorization.objects.filter(customerID=customerID, cotizacionID=cotizacionID).first()

    if existing:
        pdf_path = os.path.join(settings.CUSTOMER_AUTORIZACIONES_DIR, existing.fileName)
        if not os.path.exists(pdf_path):
            return Response({'error': 'El archivo registrado no existe en disco'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        with open(pdf_path, "rb") as pdf_file:
            pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')

        return Response({
            'fileName': existing.fileName,
            'base64': pdf_base64
        }, status=status.HTTP_200_OK)

    # No existe, generamos el archivo PDF
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"Auth_{customerID}_{timestamp}.pdf"

    context = {
        'customerID': customerID,
        'cotizacionID': cotizacionID,
        'fecha': now().strftime('%d/%m/%Y %H:%M:%S')
    }

    pdf_path = generate_pdf_from_html(context, filename)
    if not pdf_path:
        return Response({'error': 'No se pudo generar el PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    with open(pdf_path, "rb") as pdf_file:
        pdf_base64 = base64.b64encode(pdf_file.read()).decode('utf-8')

    # Guardar en base de datos
    CustomerAuthorization.objects.create(
        customerID=customerID,
        cotizacionID=cotizacionID,
        fileName=filename,
        created_by=created_by,
        created_at=now()
    )

    return Response({
        'fileName': filename,
        'base64': pdf_base64
    }, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def actualizar_autorizacion(request):
    customerID = request.data.get('customerID')
    cotizacionID = request.data.get('cotizacionID')
    nit_customer = request.data.get('nit_customer')
    nit_name = request.data.get('nit_name')
    auth_yn = request.data.get('auth_yn')
    updated_by = request.data.get('updated_by', 0)

    try:
        auth = CustomerAuthorization.objects.get(customerID=customerID, cotizacionID=cotizacionID)
        auth.nit_customer = nit_customer
        auth.nit_name = nit_name
        auth.auth_yn = auth_yn
        auth.updated_by = updated_by
        auth.updated_at = now()
        auth.save()
        return Response({'message': 'Autorización actualizada correctamente'}, status=status.HTTP_200_OK)
    except CustomerAuthorization.DoesNotExist:
        return Response({'error': 'No se encontró el registro'}, status=status.HTTP_404_NOT_FOUND)