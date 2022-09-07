from rest_framework import serializers, status
from remyapi.models import Choice
from remyapi.models import Situation

class SituationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Situation
        fields = ('id','text','location') 