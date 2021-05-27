from django.db import models

# Create your models here.


class Email(models.Model):
    content = models.CharField(max_length=200)
