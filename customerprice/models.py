# customerprice/models.py
from django.db import models

class VwCustomerPrice(models.Model):
    #fid = models.IntegerField(primary_key=True)
    cotizacionID = models.IntegerField(primary_key=True)
    customer = models.CharField(max_length=50)
    tipoPersona = models.CharField(max_length=255, null=True)
    empresaID = models.CharField(max_length=50, null=True)
    negocioID = models.CharField(max_length=50, null=True)
    matnr = models.CharField(max_length=50, null=True)
    pspnr = models.CharField(max_length=50, null=True)
    post1 = models.CharField(max_length=255, null=True)
    maktx = models.CharField(max_length=255, null=True)
    metraje = models.CharField(max_length=50, null=True)
    metraje_par = models.CharField(max_length=50, null=True)
    nombre_parqueo = models.CharField(max_length=255, null=True)
    metraje_bod = models.CharField(max_length=50, null=True)
    nombre_bodega = models.CharField(max_length=255, null=True)
    balcon = models.CharField(max_length=50, null=True)
    reserva = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    percent_enganche = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    enganche = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    estadoInventario = models.CharField(max_length=255, null=True)
    progress = models.CharField(max_length=50, null=True)

    class Meta:
        managed = False  # Importante: es una vista, no una tabla real
        db_table = 'vwCustomerPrice'
