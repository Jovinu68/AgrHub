from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from .models import Pest, Disease, DiseasePrediction
from .serializers import PestSerializer, DiseaseSerializer, DiseasePredictionSerializer
from .permissions import IsOwnerOrStaff
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .ml.predictor import predict_disease



# =========================
# PEST
# =========================

class PestListCreateView(generics.ListCreateAPIView):
    queryset = Pest.objects.all()
    serializer_class = PestSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrStaff]


class PestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pest.objects.all()
    serializer_class = PestSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


# =========================
# DISEASE
# =========================

class DiseaseListCreateView(generics.ListCreateAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class DiseaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]

class DiseasePredictionView(generics.CreateAPIView):
    queryset = DiseasePrediction.objects.all()
    serializer_class = DiseasePredictionSerializer

    permission_classes = [IsAuthenticated]

    parser_classes = [
        MultiPartParser,
        FormParser
    ]

    def create(self, request, *args, **kwargs):

        image = request.FILES.get("image")
        crop_id = request.data.get("crop")

        # Check image
        if not image:
            return Response(
                {
                    "success": False,
                    "error": "Image is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check crop
        if not crop_id:
            return Response(
                {
                    "success": False,
                    "error": "Crop ID is required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Run AI prediction
        try:

            result = predict_disease(image)

        except Exception as e:

            return Response(
                {
                    "success": False,
                    "error": "Prediction failed.",
                    "details": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        disease_name = result["disease"]
        confidence = result["confidence"]

        # Find disease in database
        disease = Disease.objects.filter(
            name__iexact=disease_name
        ).first()

        # Create prediction record
        prediction = DiseasePrediction.objects.create(
            crop_id=crop_id,
            image=image,
            predicted_disease=disease,
            confidence=confidence
        )

        serializer = self.get_serializer(prediction)

        return Response(
            {
                "success": True,
                "message": "Disease prediction completed.",
                "prediction": serializer.data,
                "ai_result": {
                    "disease": disease_name,
                    "confidence": confidence
                }
            },
            status=status.HTTP_201_CREATED
        )    