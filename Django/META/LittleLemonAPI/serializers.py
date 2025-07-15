from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only = True)
    category = CategorySerializer(read_only = True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory','category', 'category_id']
        extra_kwargs = {
            'price' : {'min_value': Decimal('2.0')},
            'inventory' : {'min_value': 0}
        }