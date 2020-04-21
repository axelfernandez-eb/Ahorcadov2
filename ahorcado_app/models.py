from django.db import models
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
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

class Api(APIView):
    ahorcado = Ahorcado()

    def get(self, request, *args, **kwargs):
        if not self.ahorcado.is_playing:
            self.ahorcado = Ahorcado()

        return Response({'word': self.ahorcado.word,
                         'message': self.ahorcado.next_turn(),
                         'lifes': self.ahorcado.lifes,
                         'used_letters': self.ahorcado.used_letters,
                         'board': self.ahorcado.board,
                         'is_playing': self.ahorcado.is_playing})

    def post(self, request, *args, **kwargs):
        # The game may change in this point, save the new state in this variable
        message = self.ahorcado.play(request.data["letter"][0])
        return Response({'message': message,
                         'lifes': self.ahorcado.lifes,
                         'used_letters': self.ahorcado.used_letters,
                         'is_playing': self.ahorcado.is_playing,
                         'board': self.ahorcado.board})
