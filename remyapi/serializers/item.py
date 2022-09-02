from rest_framework import serializers, status
from remyapi.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','name','description')