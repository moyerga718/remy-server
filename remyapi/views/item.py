from pickle import TRUE
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from remyapi.models import Item
from remyapi.serializers import ItemSerializer

class ItemView(ViewSet):
    def list(self,request):
        """get all items"""

        items = Item.objects.all()

        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='starting')
    def starting_items(self,request):
        """Return all starting items"""

        items=Item.objects.filter(starting_item = True)
        serializer = ItemSerializer(items, many = True)
        return Response(serializer.data)