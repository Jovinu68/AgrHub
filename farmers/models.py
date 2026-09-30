from django.db import models
from django.conf import settings


class Farmer(models.Model):
    user = models.OneToOneField(
       settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="farmer_profile"
    )
    phone = models.CharField(max_length=20)
    gender = models.CharField(
        max_length=10,
        choices=[
            ("MALE", "Male"),
            ("FEMALE", "Female"),
        ]
    )
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ("ACTIVE", "Active"),
            ("INACTIVE", "Inactive"),
        ],
        default="ACTIVE"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Farm(models.Model):
    farmer = models.ForeignKey(
        Farmer,
        on_delete=models.CASCADE,
        related_name="farms"
    )
    farm_name = models.CharField(max_length=150)
    location = models.CharField(max_length=255)
    size_acres = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
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
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.farm_name


class Crop(models.Model):
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name="crops"
    )
    crop_name = models.CharField(max_length=100)
    area_planted = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    planting_date = models.DateField()
    season = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.crop_name