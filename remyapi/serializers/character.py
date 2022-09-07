from rest_framework import serializers, status
from remyapi.models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id','first_name','current_situation','items')
        depth = 1