from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Highscore
from django.contrib.auth.forms import UserCreationForm


class HighscoreView(ListView):
    model = Highscore


def register(request):
    if request.method == "POST":

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'ahorcado_app/create_user.html', {'form': form})
