from rest_framework import generics
from .models import Vitamins
from .serializers import VitaminSerializer


class VitaminListView(generics.ListAPIView):
    serializer_class = VitaminSerializer
    queryset = Vitamins.objects.all()