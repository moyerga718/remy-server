from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Q

from remyapi.models import CharacterChoice

class CharacterChoiceView(ViewSet):
    """Viewset to handle changes in character choices, AKA game flags."""

    def retrieve(self, request, pk):
        """Get single character choice object""" 