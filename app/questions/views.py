from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Fanmavzusi, Savol, Varyant
from results.models import Results
from rest_framework import status
from .serializers import FanmavzusiSerializer, SavolSerializer, ResultsSerializer

# Fanmavzusi API
class FanmavzusiListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # user = request.user
        # if user.age <= 12:
        #     quizs = Fanmavzusi.objects.Boshlangich()
        # elif 12 < user.age <= 16:
        #     quizs = Fanmavzusi.objects.Ortacha()
        # else:
        quizs = Fanmavzusi.objects.all()

        serializer = FanmavzusiSerializer(quizs, many=True)
        return Response(serializer.data)

# Savollarni olish API
class QuizDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        quiz = get_object_or_404(Fanmavzusi, pk=pk)
        savols = quiz.get_savol()
        serializer = SavolSerializer(savols, many=True)
        return Response({
            'data': serializer.data,
            'vaqti': quiz.vaqti,
        })

# Quiz natijalarini saqlash API
class SaveQuizResultsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        data = request.data
        quiz = get_object_or_404(Fanmavzusi, pk=pk)
        questions = []
        score = 0
        multip = 100 / quiz.test_soni
        resultes = []

        # Parse questions
        for question_text, user_answer in data.items():
            if question_text == 'csrfmiddlewaretoken':
                continue

            savol = Savol.objects.get(text=question_text)
            questions.append(savol)

            # Check user answer
            correct_answer = None
            for variant in savol.get_answers():
                if variant.text == user_answer:
                    if variant.tugri_yoke_natugri:
                        score += 1
                        correct_answer = user_answer
                elif variant.tugri_yoke_natugri:
                    correct_answer = variant.text

            resultes.append({
                str(savol): {
                    "user_answer": user_answer,
                    "correct_answer": correct_answer,
                }
            })

        # Calculate score
        score_ = score * multip
        Results.objects.create(quiz=quiz, user=request.user, score=score_)

        return Response({
            'passed': score_ >= quiz.utish_foizi,
            'score': score_,
            'results': resultes,
        })
