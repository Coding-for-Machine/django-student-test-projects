from rest_framework import serializers
from .models import Savol, Varyant
from quizes.models import Fanmavzusi
from results.models import Results

# Fanmavzusi serializer
class FanmavzusiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fanmavzusi
        fields = ['id', 'name', 'body', 'vaqti', 'test_soni', 'utish_foizi']

# Savol va Varyantlar serializerlari
class VaryantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Varyant
        fields = ['id', 'text', 'image', 'tugri_yoke_natugri']

class SavolSerializer(serializers.ModelSerializer):
    varyants = VaryantSerializer(many=True, source='varyant_set')
    
    class Meta:
        model = Savol
        fields = ['id', 'text','image', 'savol_turi', 'varyants', 'fan_yoke_mavzu']

# Results serializer
class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ['id', 'quiz', 'user', 'score', 'date_created']
