from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from remyapi.models import Character
from remyapi.models import Situation
from remyapi.models import CharacterChoice
from remyapi.models import Choice
from remyapi.models import Item
from django.contrib.auth.models import User

from remyapi.serializers.character import CharacterSerializer

class CharacterView(ViewSet):
    def list(self,request):
        """Get all characters"""

        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Get single character"""

        character = Character.objects.get(pk=pk)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    def create(self, request):
        """Handle create new character"""
        user = request.auth.user
        important_choices = Choice.objects.filter(important = True)
        current_situation = Situation.objects.get(pk = 1)
        character = Character.objects.create(
            user = user,
            first_name = request.data['first_name'],
            current_situation = current_situation,
        )
        character.items.add(*request.data['items'])
        for choice in important_choices:
            CharacterChoice.objects.create(
                character = character,
                choice = choice,
                chosen = False
        )

        serializer = CharacterSerializer(character)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """update character. This will be called whenever a choice is selected for a situation.
        Along with characterId, client will also be sending outcomeId (resulting situation) and 
        possibly itemId (if character gets a new item from the choice) as query parameters.
        """
        #Get character
        character = Character.objects.get(pk = pk)

        #get data from query parameters
        outcomeId = request.query_params.get('outcome', None)
        itemId = request.query_params.get('item', None)

        #get situation object based on outcome id. This call will always have this query parameter, so no need for if statement
        new_situation = Situation.objects.get(pk = outcomeId)
        character.current_situation = new_situation

        #If url has itemId query parameter... 
        if itemId is not None: 
            #add that item to character
            # item = Item.objects.get(pk = itemId)
            character.items.add(itemId)

        #save the character.
        character.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """delete character"""
        character = Character.objects.get(pk = pk)
        character.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods = ['get'], detail = False, url_path='my_characters')
    def my_characters(self, request):
        user = request.auth.user
        my_characters = Character.objects.filter(user = user)
        serializer = CharacterSerializer(my_characters, many = True)
        return Response(serializer.data)

