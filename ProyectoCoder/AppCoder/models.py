from django.db import models

# Create your models here.


class Familiar(models.Model):
    nombref= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()
    Edad=models.IntegerField()