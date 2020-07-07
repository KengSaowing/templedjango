from rest_framework import serializers
from .models import temple
from .models import Category
class TempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = temple
        fields = ('name', 'Monk', 'Details', 'image',)
class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
