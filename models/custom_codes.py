from django.db import models

# Create your models here.


class CustomCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    javascript = models.CharField(max_length=1000, default="")
    css_styles = models.CharField(max_length=1000, default="")
