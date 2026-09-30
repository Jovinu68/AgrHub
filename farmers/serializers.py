from .models import Farm, Farmer, Crop
from rest_framework import serializers

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Farmer
        fields=["id",
            "user",
            "phone",
            "gender",
            "region",
            "district",
            "ward",
            "village",
            "status",
            "created_at",
            "updated_at",]
        read_only_fields = [
            "created_at",
            "updated_at",
        ]

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model=Farm
        fields=["id",
            "farmer",
            "farm_name",
            "location",
            "size_acres",
            "latitude",
            "longitude",
            "created_at",]
        read_only_fields = [
            "created_at",
        ]


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model=Crop
        fields= ["id",
            "farm",
            "crop_name",
            "area_planted",
            "planting_date",
            "season",
            "created_at",
        ]

        read_only_fields = [
            "created_at",
        ]            