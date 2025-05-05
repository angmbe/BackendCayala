from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoDeDocumentoViewSet

router = DefaultRouter()
router.register(r'tipos-documento', TipoDeDocumentoViewSet, basename='tipodocumento')

urlpatterns = [
    path('', include(router.urls)),
]