from django.db import models

# Create your models here.
class Inasistencia(models.Model):
	gafete_i = models.PositiveIntegerField()
	idevento_i = models.PositiveIntegerField()
	fecha_i = models.DateTimeField()

	def __unicode__(self):
		return unicode(self.gafete_i)