from django.urls import include, path
from .views import HighscoreView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('highscore/', HighscoreView.as_view(), name='highscores'),
]
