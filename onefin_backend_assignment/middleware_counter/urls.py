from django.urls import path
from middleware_counter.views import (
    CounterRequest, ResetCounterRequest
)

urlpatterns = [
    path('request-count', CounterRequest.as_view()),
    path('request-count/reset', ResetCounterRequest.as_view()),

]
