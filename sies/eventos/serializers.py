from rest_framework import serializers

from .models import Evento

class EventSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Evento	