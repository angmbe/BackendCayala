from django.urls import path
from . import views

urlpatterns = [
    path('customerpayment/register/', views.register_payment),
    path('customerpayment/getfile/', views.get_payment_file_base64),
    path('customerpayment/update/', views.update_payment),
    path('customerpayment/', views.get_payments_by_customer),
]