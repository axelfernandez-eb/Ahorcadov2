from django.urls import include, path

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('highscore/', HighscoreView.as_view(), name='highscores'),
]
