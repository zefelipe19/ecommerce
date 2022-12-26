from rest_framework import serializers
from .models import Item, ItemOrder


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'get_promotional_price', 'description')