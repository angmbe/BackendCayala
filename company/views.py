from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer

@api_view(['GET'])
def get_all_company(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_company_by_id(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CompanySerializer(company)
    return Response(serializer.data)


# @api_view(['GET'])
# def get_customer_by_nit(request, nit):
#     try:
#         customer = Customer.objects.get(nit=nit)
#     except Customer.DoesNotExist:
#         return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

#     serializer = CustomerSerializer(customer)
#     return Response(serializer.data)

@api_view(['POST'])
def update_company(request, id):
    try:
        company = Company.objects.get(pk=id)
    except Company.DoesNotExist:
        return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CompanySerializer(company, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)