from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=50)
    user_password = models.CharField(max_length=20)
    active = models.BooleanField(default=True)



   
