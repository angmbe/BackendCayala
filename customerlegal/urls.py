from django.urls import path
from . import views

urlpatterns = [
    path('customerlegal/upload/', views.upload_document, name='upload_document'),
    path('customerlegal/base64/', views.get_document_base64, name='get_document_base64'),
    path('customerlegal/test/', views.test_post),
    path('customerlegal/update/', views.approved_document, name='approved_document'),
    path('customerlegal/<str:customerID>/', views.get_documents_by_customer, name='get_documents_by_customer'),
]