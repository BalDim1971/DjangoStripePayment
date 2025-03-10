from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Item
    """

    class Meta:
        model = Item
        fields = '__all__'
