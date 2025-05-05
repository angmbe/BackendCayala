from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.get_all_customers, name='get_all_customers'),
    path('customers/<str:id>/', views.get_customer_by_id, name='get_customer_by_id'),
    path('customers/update/<str:id>/', views.update_customer, name='update_customer'),
]
