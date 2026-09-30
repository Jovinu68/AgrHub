from rest_framework import serializers
from . models import Pest, Disease, DiseasePrediction

class PestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pest
        fields='__all__'

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Disease
        fieds='__all__'        

class DiseasePredictionSerializer(serializers.ModelSerializer):
    predicted_disease_name = serializers.CharField(
        source="predicted_disease.name",
        read_only=True
    )

    class Meta:
        model = DiseasePrediction
        fields = [
            "id",
            "crop",
            "image",
            "predicted_disease",
            "predicted_disease_name",
            "confidence",
            "created_at",
        ]
        read_only_fields = [
            "predicted_disease",
            "predicted_disease_name",
            "confidence",
            "created_at",
        ]        