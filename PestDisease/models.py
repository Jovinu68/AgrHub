from django.db import models

# Create your models here.

from django.db import models


class Pest(models.Model):
    name = models.CharField(max_length=150)
    scientific_name = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    symptoms = models.TextField(
        blank=True,
        null=True
    )
    affected_crops = models.TextField(
        blank=True,
        null=True
    )
    severity = models.CharField(
        max_length=20,
        choices=[
            ("LOW", "Low"),
            ("MEDIUM", "Medium"),
            ("HIGH", "High"),
            ("CRITICAL", "Critical"),
        ],
        default="LOW"
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=150)
    scientific_name = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    symptoms = models.TextField(
        blank=True,
        null=True
    )
    affected_crops = models.TextField(
        blank=True,
        null=True
    )
    severity = models.CharField(
        max_length=20,
        choices=[
            ("LOW", "Low"),
            ("MEDIUM", "Medium"),
            ("HIGH", "High"),
            ("CRITICAL", "Critical"),
        ],
        default="LOW"
    )
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    



class DiseasePrediction(models.Model):
    crop = models.ForeignKey(
        "farmers.Crop",
        on_delete=models.CASCADE,
        related_name="disease_predictions"
    )
    image = models.ImageField(
        upload_to="disease_predictions/"
    )
    predicted_disease = models.ForeignKey(
        Disease,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="predictions"
    )
    confidence = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

class PestDiseaseReport(models.Model):

    SEVERITY_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
        ("CRITICAL", "Critical"),
    ]

    farmer = models.ForeignKey(
        "farmers.Farmer",
        on_delete=models.CASCADE,
        related_name="pest_disease_reports"
    )

    farm = models.ForeignKey(
        "farmers.Farm",
        on_delete=models.CASCADE,
        related_name="pest_disease_reports"
    )

    crop = models.ForeignKey(
        "farmers.Crop",
        on_delete=models.CASCADE,
        related_name="pest_disease_reports"
    )

    pest = models.ForeignKey(
        Pest,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reports"
    )

    disease = models.ForeignKey(
        Disease,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reports"
    )
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default="LOW"
    )
    image = models.ImageField(
        upload_to="pest_disease_reports/",
        null=True,
        blank=True
    )
    report_date = models.DateTimeField(
        auto_now_add=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    def __str__(self):
        return f"{self.crop} - {self.location} - {self.severity}"    