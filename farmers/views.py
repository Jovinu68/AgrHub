from django.shortcuts import render
from . serializers import CropSerializer, FarmerSerializer, FarmSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . models import Farm, Farmer, Crop
from .permissions import IsOwnerOrStaff


# =========================
# FARMER
# =========================

class FarmerListCreateView(ListCreateAPIView):
    serializer_class = FarmerSerializer
    permission_classes = [IsOwnerOrStaff]
    def get_queryset(self):
        user = self.request.user
        if user.role in ["ADMIN", "OFFICER", "INSPECTOR"]:
            return Farmer.objects.all()
        return Farmer.objects.filter(user=user)


class FarmerDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsOwnerOrStaff]


# =========================
# FARM
# =========================

class FarmListCreateView(ListCreateAPIView):
    serializer_class = FarmSerializer
    permission_classes = [IsOwnerOrStaff]
    def get_queryset(self):
        user = self.request.user
        if user.role in ["ADMIN", "OFFICER", "INSPECTOR"]:
            return Farm.objects.all()
        return Farm.objects.filter(farmer__user=user)


class FarmDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsOwnerOrStaff]


# =========================
# CROP
# =========================

class CropListCreateView(ListCreateAPIView):
    serializer_class = CropSerializer
    permission_classes = [IsOwnerOrStaff]
    def get_queryset(self):
        user = self.request.user
        if user.role in ["ADMIN", "OFFICER", "INSPECTOR"]:
            return Crop.objects.all()
        return Crop.objects.filter(
            farm__farmer__user=user
        )


class CropDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [IsOwnerOrStaff]