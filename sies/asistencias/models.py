from django.db import models  

# Create your models here.
class Asistencia(models.Model):
	gafete_a = models.PositiveIntegerField()
	idevento_a = models.PositiveIntegerField()
	fecha_a = models.DateTimeField()

	def __unicode__(self):
		return unicode(self.gafete_a)