from django.db import models
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .ahorcado import Ahorcado


class Highscore(models.Model):
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="name",
    )
    lifes = models.IntegerField()
    word = models.CharField(max_length=20)


class Game(APIView):
    word = Ahorcado().get_word_from_api()

    def __init__(self, *args, **kwargs):
        self.ahorcado = Ahorcado(self.word)

    def get(self, request, *args, **kwargs):
        return Response({self.ahorcado.word+self.ahorcado.next_turn()})

    def post(self, request, *args, **kwargs):
        return Response({self.ahorcado.play(**request.data)})
