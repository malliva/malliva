from django.db import models

# Create your models here.
class CustomCode(models.Model):
    content = models.CharField(max_length=500)
