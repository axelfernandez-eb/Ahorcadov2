from django.db import models
from django.conf import settings



class Highscore(models.Model):
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="name",
    )
    lifes = models.IntegerField()
    word = models.CharField(max_length=20)
# Create your models here.
