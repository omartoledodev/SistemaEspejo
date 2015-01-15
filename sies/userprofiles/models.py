from django.db import models 
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	gafete = models.PositiveSmallIntegerField(unique=True) 
	avatar = models.ImageField(upload_to='profiles')
	GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
	genero = models.CharField(max_length=1, choices=GENDER_CHOICES) 

	def __unicode__(self):
 		return unicode(self.apellido) or u''