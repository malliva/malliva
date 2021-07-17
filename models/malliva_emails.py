from django.db import models

# Create your models here.

# capture sent emails and templates


class Email(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.CharField(max_length=200)
