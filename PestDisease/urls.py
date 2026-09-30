from django.urls import path
from .import views

urlpatterns = [
    path('Disease/', views.DiseaseListCreateView.as_view()),
    path('Disease/<str:pk>/', views.DiseaseDetailView.as_view()),
    path('Pest/', views.PestListCreateView.as_view()),
    path('Pest/<str:pk>/', views.PestDetailView.as_view()),
    path('predict/', views.DiseasePredictionView.as_view())

]