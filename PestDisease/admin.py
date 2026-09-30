from django.contrib import admin
from . models import Pest, Disease, PestDiseaseReport, DiseasePrediction
# Register your models here.

admin.site.register(Pest)
admin.site.register(Disease)
admin.site.register(PestDiseaseReport)
admin.site.register(DiseasePrediction)

