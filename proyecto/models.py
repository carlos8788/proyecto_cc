from django.db import models

# Create your models here.
class Proyecto(models.Model):
    id = models.CharField(auto_created=False, primary_key=True, max_length=100)
    nombre = models.CharField(max_length=200)
    permiso = models.BooleanField()