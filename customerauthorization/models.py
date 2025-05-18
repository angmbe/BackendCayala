from django.db import models
from django.utils import timezone

class CustomerAuthorization(models.Model):
    id_auth =  models.AutoField(primary_key=True)
    customerID = models.CharField(max_length=20)
    cotizacionID = models.IntegerField()
    fileName = models.TextField()
    nit_customer = models.CharField(max_length=20, null=True, blank=True)
    nit_name = models.CharField(max_length=100, null=True, blank=True)
    auth_yn = models.CharField(max_length=1, null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'CustomerAuthorization'
        managed = False