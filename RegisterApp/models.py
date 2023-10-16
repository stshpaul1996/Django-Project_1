from django.db import models

# Create your models here.
class RegisterDB(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.IntegerField()
    address = models.TextField()