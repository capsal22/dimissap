from django.shortcuts import render
from .models import Candidato, Previsione

def home(request):
    candidati = Candidato.objects.all()
    previsioni = Previsione.objects.all()
    return render(request, "index.html", {"candidati": candidati, "previsioni": previsioni})
