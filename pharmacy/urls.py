from django.urls import path
from .views import PharmacyRatingView, PharmacyReviewView, PharmacyListAPIView, PharmacyDetailAPIView

app_name = 'pharmacy'

urlpatterns = [
    path('rating/<int:pharmacy_id>/', PharmacyRatingView.as_view()),
    path('review/<int:pharmacy_id>/', PharmacyReviewView.as_view()),
    path('list/', PharmacyListAPIView.as_view()),
    path('list/<int:id>/detail/', PharmacyDetailAPIView.as_view()),
]