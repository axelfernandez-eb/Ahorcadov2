from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Highscore


class HighscoreView(ListView):
    model = Highscore


# Create your views here.
