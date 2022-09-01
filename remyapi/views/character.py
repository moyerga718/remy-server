from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from remyapi.models import Character
from remyapi.models import Situation
from django.contrib.auth.models import models

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
        current_situation = Situation.objects.get(pk = 1)
        character = Character.objects.create(
            user = user,
            first_name = request.data['first_name'],
            current_situation = current_situation,
        )
        character.items.add(*request.data['items'])

        serializer = CharacterSerializer(character)
        return Response(serializer.data)

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

