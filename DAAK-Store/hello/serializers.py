from rest_framework import serializers 

from gamestore.models import * 

from hello.models import * 


class ScoreSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Score



		fields = ('score', )

