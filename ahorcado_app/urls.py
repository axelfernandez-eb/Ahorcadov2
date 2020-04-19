from django.urls import include, path
from .models import Game
from .views import HighscoreView


urlpatterns = [
    path('', include('django.contrib.auth.urls'), name="login"),
    path('highscore/', HighscoreView.as_view(), name='highscores'),
    path('game', Game.as_view(), name='game')
]
