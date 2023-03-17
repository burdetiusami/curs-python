from django.db import models

class Trucks(models.Model):
    truck_make = models.CharField(max_length=30)
    truck_model = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    truck_image = models.ImageField(null=True, blank=True, upload_to='media/truck-images/')
    status = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Trailers(models.Model):
    trailer_make = models.CharField(max_length=30)
    trailer_model = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    trailer_image = models.ImageField(null=True, blank=True, upload_to='media/trailer-images/')
    status = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
