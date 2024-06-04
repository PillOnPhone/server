from rest_framework import serializers
from .models import Vitamins


class VitaminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitamins
        fields = '__all__'