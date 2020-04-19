from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Highscore, Game
from .ahorcado import Ahorcado


class HighscoreView(ListView):
    model = Highscore
