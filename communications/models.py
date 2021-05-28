from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import DO_NOTHING

User = get_user_model()

# Create your models here.
class Message(models.Model):
    initiated_by = models.ForeignKey(User, on_delete=DO_NOTHING, blank=False)
    # received_by = models.ForeignKey(User, on_delete=DO_NOTHING, blank=False)
