from django.db import models 

# Create your models here.
class ConceptoSancion(models.Model):
	nombre = models.CharField(max_length=50)
	cantidad = models.PositiveIntegerField()

	def __unicode__(self):
		return unicode(self.nombre)