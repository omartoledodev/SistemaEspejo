from django.db import models 

# Create your models here.
class ConceptoExtra(models.Model):
	nombre = models.CharField(max_length=200)
	cantidad = models.PositiveIntegerField()

	def __unicode__(self):
		return unicode(self.nombre)