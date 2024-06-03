from django.urls import path
from .views import PharmacyRatingView, PharmacyReviewView

app_name = 'pharmacy'

urlpatterns = [
    path('rating/<int:pharmacy_id>/', PharmacyRatingView.as_view()),
    path('review/<int:pharmacy_id>/', PharmacyReviewView.as_view())
]