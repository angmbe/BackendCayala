from django.db import models

class ListOfItemValue(models.Model):
    valueID = models.AutoField(primary_key=True)
    listID = models.IntegerField()
    descriptionValue = models.CharField(max_length=100)
    itemValue = models.CharField(max_length=20)
    hsValue = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'ListOfItemValue'  # Esta línea evita que Django cree una tabla nueva
        managed = False 