from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Q

from remyapi.models import CharacterChoice

class CharacterChoiceView(ViewSet):
    """Viewset to handle changes in character choices, AKA game flags."""

    @action(methods=['put'], detail=True)
    def chosen(self,request,pk):
        """This action locates a character_choice object based on choice ID and character ID and flips chosen to TRUE
        """
        characterId = request.query_params.get('character', None)
        try:
            character_choice = CharacterChoice.objects.get(choice_id=pk, character_id=characterId)
            character_choice.chosen = True
            character_choice.save()
        except:
            pass
        return Response(None, status=status.HTTP_204_NO_CONTENT)
