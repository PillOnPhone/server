from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializer import PharmacyRatingSerializer
from .models import Pharmacy_Review
from rest_framework import status

# Create your views here.

class PharmacyRatingView(CreateAPIView):
    serializer_class = PharmacyRatingSerializer
    
    def get(self, request, *args, **kwargs):
        pharmacy_id = self.kwargs.get('pharmacy_id')
        review = Pharmacy_Review.objects.filter(pharmacy_id=pharmacy_id).values()
        rating_str = ['rating_1', 'rating_2', 'rating_3', 'rating_4', 'rating_5']
        rating_int = [0,0,0,0,0]
        for i in review:
            rating_int[i['rating'] - 1] += 1
        if(max(rating_int) != 0): 
            result = dict(zip(rating_str, rating_int))
            return Response({
                'success' : True,
                'code' : 200,
                'message' : "요청에 성공하셨습니다.",
                'rating' : result
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success' : False,
                'code' : 404,
                'message' : "리뷰 데이터가 존재하지 않습니다.",
                }, status=status.HTTP_404_NOT_FOUND)
    

class PharmacyReviewView(CreateAPIView):
    serializer_class = PharmacyRatingSerializer

    def get_queryset(self):
        pharmacy_id = int(self.kwargs.get('pharmacy_id'))
        return Pharmacy_Review.objects.filter(pharmacy_id=pharmacy_id)
    
    def get(self, request, *args, **kwargs):
        pharmacy_id = self.kwargs.get('pharmacy_id')
        review = Pharmacy_Review.objects.filter(pharmacy_id=pharmacy_id).values()
        result = []
        for i in review:
            result.append(i)
        if (result != []):
            return Response({
                'success' : True,
                'code' : 200,
                'message' : "요청에 성공하셨습니다.",
                'rating' : result
                }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success' : False,
                'code' : 404,
                'message' : "리뷰 데이터가 존재하지 않습니다.",
                }, status=status.HTTP_404_NOT_FOUND)