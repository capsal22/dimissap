from django.db import models
from django.contrib.auth.models import User

class Candidato(models.Model):
    nome = models.CharField(max_length=255)
    ruolo = models.CharField(max_length=255)
    immagine = models.CharField(max_length=255,null=True)
    in_carica = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.ruolo})"

class Previsione(models.Model):
    utente = models.ForeignKey(User, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    data_prevista = models.DateField()

class Risultato(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    data_dimissioni = models.DateField(null=True, blank=True)
