from rest_framework import generics
from pill.serializers import VitaminSerializer
from .models import Pharmacy, Pharmacist, PharmacyVitamins
from .serializers import PharmacySerializer, PharmacySerializerdetail, PharmacistSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializer import PharmacyRatingSerializer
from .models import Pharmacy_Review
from rest_framework import status


class PharmacyListAPIView(generics.ListAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    #filter_backends = [filters.OrderingFilter]
    #ordering_fields = ['id','title']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # 약국 목록 존재 여부 확인
        if not queryset.exists():
            return Response({
                'success': False,
                'code': 404,
                'message': "약국 데이터가 존재하지 않습니다.",
            }, status=status.HTTP_404_NOT_FOUND)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)  # 페이지네이션 적용
        else:
            serializer = self.get_serializer(queryset, many=True)  # 전체 데이터 직렬화

        print(serializer.data)
        return Response({
            'success': True,
            'code': 200,
            'message': "요청에 성공하셨습니다.",
            'pharmacies': serializer.data
        }, status=status.HTTP_200_OK)

class PharmacyDetailAPIView(generics.RetrieveAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializerdetail
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        #약국 id에 해당하는 약사 불러오기
        pharmacists = Pharmacist.objects.filter(pharmacy_id=instance.id)
        #약국 id에 해당하는 vitamin의 목록을 가져오기
        pharmacyvitamins = PharmacyVitamins.objects.filter(pharmacy_id=instance.id).select_related('vitamin_id')
        vitamins = [pv.vitamin_id for pv in pharmacyvitamins]

        pharmacy_serializer = PharmacySerializerdetail(instance=instance)
        pharmacist_serializer = PharmacistSerializer(pharmacists, many=True)
        vitamins_serializer = VitaminSerializer(vitamins, many=True)

        data = {
            'pharmacists': pharmacist_serializer.data,
            'pharmacyvitamins': vitamins_serializer.data
        }

        return Response({
            'success': True,
            'code': 200,
            'message': "요청에 성공하셨습니다.",
            'pharmacy': pharmacy_serializer.data,
            'pharmacydetail': data
        }, status=status.HTTP_200_OK)


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
