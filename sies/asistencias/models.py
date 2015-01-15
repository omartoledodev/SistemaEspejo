from django.db import models

# Create your models here.
class Asistencia(models.Model):
	idusuario = models.PositiveIntegerField()
	clave_evento = models.PositiveIntegerField()

	def __unicode__(self):
		self.clave_evento=str(self.clave_evento)
		return self.clave_evento 