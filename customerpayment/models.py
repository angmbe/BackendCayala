from django.db import models

class CustomerPayment(models.Model):
    paymentID = models.AutoField(primary_key=True)
    customerID = models.CharField(max_length=10)
    cotizacionID = models.IntegerField(null=True, blank=True)
    paymentDate = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentType = models.CharField(max_length=50, null=True, blank=True)
    operationNumber = models.CharField(max_length=100, null=True, blank=True)
    fileName = models.TextField(null=True, blank=True)
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=False)
    created_by = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'CustomerPayment'
        managed = False