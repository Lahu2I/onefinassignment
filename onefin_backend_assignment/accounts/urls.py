from django.urls import path
from accounts.apiviews.register import RegisterUserAPIView

urlpatterns = [
    path('', RegisterUserAPIView.as_view()),
]
