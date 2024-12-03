from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Savol
from .serializers import SavolSerializer

@api_view(['GET'])
def get_savol(request):
    # Filter questions by difficulty if provided, else return all
    difficulty = request.query_params.get('difficulty', None)
    if difficulty == "ASN":
        savols = Savol.objects.Asanroq()
    elif difficulty == "ORT":
        savols = Savol.objects.Ortacha()
    elif difficulty == "QYN":
        savols = Savol.objects.Qiyin()
    else:
        savols = Savol.objects.all()

    # Serialize the questions
    serializer = SavolSerializer(savols, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def submit_savol_result(request):
    # Placeholder to process quiz results
    score = request.data.get('score', 0)
    return Response({"message": "Result received", "score": score})
