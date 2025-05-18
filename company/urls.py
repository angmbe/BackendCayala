from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.get_all_company, name='get_all_company'),
    path('company/<str:id>/', views.get_company_by_id, name='get_company_by_id'),
    path('company/update/<str:id>/', views.update_company, name='update_company'),
    #path('company/nit/<str:nit>/', views.get_customer_by_nit, name="get_customer_by_nit"),
]
