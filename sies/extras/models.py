from django.db import models 
from userprofiles.models import UserProfile
from cextras.models import ConceptoExtra 

# Create your models here.
class Extra(models.Model):
	empleado = models.ForeignKey(UserProfile)
	concepto = models.ForeignKey(ConceptoExtra) 

	def __unicode__(self):
		return unicode(self.empleado)