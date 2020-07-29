from rest_framework import serializers
from .models import temple
from .models import Category
class TempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = temple
        fields = "__all__"
class  CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
