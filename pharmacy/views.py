from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializer import PharmacyReviewSerializer
from .models import Pharmacy_Review
from rest_framework import status

# Create your views here.

class PharmacyReviewView(CreateAPIView):
    serializer_class = PharmacyReviewSerializer
    # queryset = Pharmacy_Review.objects.all()

    # def get_object(self):
    #     pharmacy_id = self.kwargs.get('pharmacy_id')
    #     return get_object_or_404(Pharmacy_Review, pharmacy_id=pharmacy_id)

    def get_queryset(self):
        pharmacy_id = int(self.kwargs.get('pharmacy_id'))
        return Pharmacy_Review.objects.filter(pharmacy_id=pharmacy_id)
    
    def get(self, request, *args, **kwargs):
        # try:
        pharmacy_id = self.kwargs.get('pharmacy_id')
        review = Pharmacy_Review.objects.filter(pharmacy_id=pharmacy_id)
        serializer = self.serializer_class(review, data=request.data, partial=True, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # except:
        #     return Response({
        #         'success' : False
        #     })