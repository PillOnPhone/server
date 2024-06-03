from rest_framework import serializers
from .models import Pharmacy_Review

class PharmacyRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy_Review
        fields = '__all__'