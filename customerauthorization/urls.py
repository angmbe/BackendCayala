from django.urls import path
from . import views

urlpatterns = [
    path('customerauthorization/generar/', views.generar_autorizacion_pdf),
    path('customerauthorization/actualizar/', views.actualizar_autorizacion),
]