from django.db import models
from django.conf import settings
from rest_framework.views import APIView

class Highscore(models.Model):
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="name",
    )
    lifes = models.IntegerField()
    word = models.CharField(max_length=20)


class Game(APIView):
    def get(self, request, *args, **kwargs):
        return 'implement this Too'

    def post(self, request, *args, **kwargs):
        return 'Implement this'