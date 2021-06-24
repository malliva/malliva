from django.db import models

# Create your models here.


class Email(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=200)
