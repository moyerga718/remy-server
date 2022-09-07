from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Q

from remyapi.models import Situation
from remyapi.models import Choice
from remyapi.models import Character
from remyapi.serializers import SituationSerializer
from remyapi.serializers import ChoiceSerializer

class ChoiceView(ViewSet):

    @action(methods=['get'], detail=True)
    def valid_choices(self, request, pk):
        """method to handle returning a situation AND corresponding choices that match criteria."""
        characterId = request.query_params.get('character', None)
        # Get situation matching pk, run through serializer
        situation = Situation.objects.get(pk=pk)

        # Get all choices for current situation
        situation_choices = Choice.objects.filter(situation = situation)

        if characterId is not None:
            character = Character.objects.get(pk=characterId)
            # Filter by whether choice has an affiliated character_choice object. If it does not, return it. If it does, check to see if that choice has already been selected by that character. If not, return that choice.
            choices_by_character_flag = situation_choices.filter( Q(important = False) | Q(character_choices__chosen=False, character_choices__character_id=characterId))
            choices_by_item_req = choices_by_character_flag.filter(Q(required_item_bool=False) | Q(required_item_id__in = character.items.all()))
            
        situation_choices_serializer = ChoiceSerializer(choices_by_item_req, many=True)

        return Response(situation_choices_serializer.data)