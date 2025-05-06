from django.db import models

class CustomerLegal(models.Model):
    legalID = models.AutoField(primary_key=True)
    customerID = models.CharField(max_length=50)
    documentID = models.IntegerField()
    expiredDate = models.DateTimeField()
    fileName = models.TextField()
    status = models.BooleanField(default=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'CustomerLegal'
        managed = False