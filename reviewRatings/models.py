from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE, DO_NOTHING

User = get_user_model()

# Create your models here.
class reviewRating(models.Model):
    giver = models.ForeignKey(User, on_delete=DO_NOTHING)
    # receiver = models.ForeignKey(User, on_delete=CASCADE)
