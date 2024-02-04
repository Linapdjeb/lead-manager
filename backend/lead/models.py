from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    massage = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leads", null=True)
    created = models.DateTimeField(auto_now_add=True)

