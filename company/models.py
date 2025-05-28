from django.db import models

class Company(models.Model):
    empresaID = models.CharField(primary_key=True, max_length=50)
    company_name = models.CharField(max_length=150, null=True)
    nit_empresa = models.CharField(max_length=150, null=True)
    company_address = models.CharField(max_length=100, null=True)
    number_address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    correo_electronico_c = models.CharField(max_length=255, null=True)
    industry = models.CharField(max_length=255, null=True)
    nombre_representante_legal = models.CharField(max_length=255, null=True)
    identificacion_representante = models.CharField(max_length=255, null=True)
    estado_civil_rl = models.CharField(max_length=255, null=True)
    lugar_de_nacimiento = models.CharField(max_length=255, null=True)
    direccion_rl = models.CharField(max_length=255, null=True)
    profesion_rl = models.CharField(max_length=255, null=True)
    fecha_nacimiento_rl = models.CharField(max_length=255, null=True)
    edad_rl = models.IntegerField()
    genero_rl = models.IntegerField()
    ingresos_mensuales = models.CharField(max_length=255, null=True)
    rango_egresos_mensuales = models.CharField(max_length=255, null=True)
    mascotas_yn = models.CharField(max_length=1, null=True)
    tipo_mascota = models.IntegerField()
    beneficiario_final = models.CharField(max_length=255, null=True)
    relacion_gobierno = models.CharField(max_length=255, null=True)
    forma_pago = models.IntegerField()
    uso_empresa = models.CharField(max_length=255, null=True)
    datos_complementarios = models.CharField(max_length=255, null=True)
    datos_comerciales = models.CharField(max_length=255, null=True)
    #create_at = models.DateTimeField(null=True)
    #status_update = models.BooleanField(null=True)

    class Meta:
        db_table = 'Company'
        managed = False

    



