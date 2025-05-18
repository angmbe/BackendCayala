from django.db import models

class Company(models.Model):
    empresaID = models.CharField(primary_key=True, max_length=50)
    company_name = models.CharField(max_length=150, null=True)
    company_address = models.CharField(max_length=100, null=True)
    number_address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    correo_electronico_c = models.CharField(max_length=255, null=True)
    industry = models.CharField(max_length=255, null=True)
    #create_at = models.DateTimeField(null=True)
    #status_update = models.BooleanField(null=True)

    class Meta:
        db_table = 'Company'
        managed = False

    



