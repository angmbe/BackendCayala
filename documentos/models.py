from django.db import models

class TipoDeDocumento(models.Model):
    id = models.IntegerField(primary_key=True)  # Asumimos que existe un campo ID
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Muy importante: NO queremos que Django intente crear o alterar esta tabla
        db_table = 'Documento'