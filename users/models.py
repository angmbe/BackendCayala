from django.db import models

class Profile(models.Model):
    profileid = models.AutoField(primary_key=True)
    profilename = models.CharField(max_length=100)
    status = models.BooleanField()
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'Profile'
        managed = False

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password_hash = models.CharField(max_length=255)  # ← NO plaintext
    fullname = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, db_column='profileID')
    customer_id = models.CharField(max_length=50, null=True)
    status = models.BooleanField()
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_by = models.IntegerField(null=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'Users'
        managed = False
