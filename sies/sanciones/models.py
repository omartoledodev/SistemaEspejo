from django.db import models 
from userprofiles.models import UserProfile
from csanciones.models import ConceptoSancion

# Create your models here.
class Sancion(models.Model):
	empleado = models.ForeignKey(UserProfile)
	concepto = models.ForeignKey(ConceptoSancion) 

	def __unicode__(self):
		return unicode(self.empleado)
 