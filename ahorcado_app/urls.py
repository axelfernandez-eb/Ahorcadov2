from django.urls import include, path
from .models import Api
from .views import HighscoreView, register, game_view

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name="login"),
    path('highscore/', HighscoreView.as_view(), name='highscores'),
    path('game/', game_view),
    path('api/', Api.as_view(), name='api'),
    path('register/',register, name='register'),
]
