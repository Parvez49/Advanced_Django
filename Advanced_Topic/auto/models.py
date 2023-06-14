from django.db import models

# Create your models here.


# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField( max_length=50)
    bio=models.CharField( max_length=50)