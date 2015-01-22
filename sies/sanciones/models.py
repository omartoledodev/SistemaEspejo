from django.db import models 
from userprofiles.models import UserProfile


# Create your models here.
class Sancion(models.Model):
	gafete_s = models.PositiveIntegerField()
	cantidad_s = models.PositiveIntegerField()
	fecha_s = models.DateField()
