from django.db import models

# Create your models here.
class Lista(models.Model):
	idusuario = models.PositiveIntegerField()
	gafete_l = models.PositiveIntegerField()
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	clave_evento = models.PositiveIntegerField()
	evento = models.CharField(max_length=250)

	def __unicode__(self):
		return self.evento