from django.urls import path
from .views import CreateChattingRoom

urlpatterns = [
    path('create/', CreateChattingRoom.as_view()),
]