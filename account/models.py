from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLES_CHOICE=[
        ('Admin','ADMIN'),
        ('OFFICER', 'Agriculture Officer'),
        ('INSPECTOR','Inspector'),
        ('FARMER','Farmer')
    ]

    role=models.CharField(max_length=20, choices=ROLES_CHOICE, default='farmer')
    phone=models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username}-- {self.role}"
