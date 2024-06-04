from rest_framework import serializers
from .models import Pharmacy, Pharmacist


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['title', 'image', 'location']


class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = '__all__'


class PharmacySerializerdetail(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'