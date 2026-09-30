from django.contrib import admin
from . models import Farm, Farmer, Crop

# Register your models here.
admin.site.register(Farmer)
admin.site.register(Crop)
admin.site.register(Farm)
