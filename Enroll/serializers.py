from rest_framework import serializers
from .models import temple

class TempleSerializer(serializers.ModelSerializer):
    class Meta:
        model = temple
        fields = ('name', 'Monk', 'Details', 'image','Category',)