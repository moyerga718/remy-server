from rest_framework import serializers, status
from remyapi.models import CharacterChoice

class CharacterChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterChoice
        fields = ('id')