from django.urls import path
from .views import ListItemsByListID

urlpatterns = [
    path('items/<int:list_id>/', ListItemsByListID.as_view(), name='items-by-listid'),
]