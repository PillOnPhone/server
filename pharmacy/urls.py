from django.urls import path
from .views import PharmacyReviewView

app_name = 'pharmacy'

urlpatterns = [
    path('rating/<int:pharmacy_id>/', PharmacyReviewView.as_view())
]