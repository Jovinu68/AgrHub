from django.urls import path

from .views import (
    FarmerListCreateView,
    FarmerDetailView,
    FarmListCreateView,
    FarmDetailView,
    CropListCreateView,
    CropDetailView,
)


urlpatterns = [

    # Farmer
    path(
        "farmers/",
        FarmerListCreateView.as_view(),
        name="farmer-list-create"
    ),

    path(
        "farmers/<int:pk>/",
        FarmerDetailView.as_view(),
        name="farmer-detail"
    ),

    # Farm
    path(
        "farms/",
        FarmListCreateView.as_view(),
        name="farm-list-create"
    ),

    path(
        "farms/<int:pk>/",
        FarmDetailView.as_view(),
        name="farm-detail"
    ),

    # Crop
    path(
        "crops/",
        CropListCreateView.as_view(),
        name="crop-list-create"
    ),

    path(
        "crops/<int:pk>/",
        CropDetailView.as_view(),
        name="crop-detail"
    ),
]