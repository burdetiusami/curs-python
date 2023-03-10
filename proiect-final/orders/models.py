from django.db import models

class Orders(models.Model):
    company = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    cargo_info = models.CharField(max_length=100)
    eta = models.DateField()
    status = models.BooleanField(default=True)
