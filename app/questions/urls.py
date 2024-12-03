from django.urls import path
from .views import FanmavzusiListAPIView, QuizDetailAPIView, SaveQuizResultsAPIView

urlpatterns = [
    path('api/quiz/', FanmavzusiListAPIView.as_view(), name='quiz-list'),
    path('quizs/<int:pk>/quizs/api/quiz/', QuizDetailAPIView.as_view(), name='quiz-detail'),
    path('api/quiz/<int:pk>/save/', SaveQuizResultsAPIView.as_view(), name='quiz-save'),
]
