from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    date_of_birth = models.DateField()
    email_adress = models.EmailField(max_length=50)