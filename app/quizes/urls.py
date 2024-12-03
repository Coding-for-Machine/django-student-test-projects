from django.urls import path
from .views import *

app_name="quizes"

urlpatterns = [
    path("",quiz_list, name="quizlist"),
    path("quizs/<str:pk>/quizs/", quiz_datiel, name="quizsdatiel"),
    path("quizs/<str:pk>/quizs/data/", quiz_data_json, name="datajson"),
    path("quizs/<str:pk>/quizs/save/", save_quiz_data, name="datasave"),
    

]

