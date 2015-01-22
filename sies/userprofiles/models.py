from django.db import models  
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class UserProfile(models.Model):
	username = models.OneToOneField(User)
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	gafete = models.PositiveSmallIntegerField(unique=True) 
	avatar = models.ImageField(upload_to='profiles')
	GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
	genero = models.CharField(max_length=1, choices=GENDER_CHOICES) 

	def foto(self):#reproductor de archivos tag <audio>
		#"""string de multiples lineas
		return """
		<img src="%s">
		""" % self.avatar.url
	foto.allow_tags = True # esta funcion se renderiza como html seguro
	foto.admin_order_field = 'avatar'#ordenar por track_file

	def __unicode__(self):
 		return unicode(self.apellido) or u''