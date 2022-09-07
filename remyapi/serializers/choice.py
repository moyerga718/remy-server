from rest_framework import serializers, status
from remyapi.models import Choice
from remyapi.models import CharacterChoice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id','situation','text', 'outcome_situation', 'get_item_bool', 'new_item', 'required_item_bool', 'required_item')