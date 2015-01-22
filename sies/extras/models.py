from django.db import models 
from userprofiles.models import UserProfile
# Create your models here.
class Extra(models.Model):
	gafete_e = models.PositiveIntegerField()
	cantidad_e = models.PositiveIntegerField() 
	fecha_e = models.DateTimeField()
