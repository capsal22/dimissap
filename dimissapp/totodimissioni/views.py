from django.shortcuts import render
from .models import Candidato, Previsione, UtentiCensiti
from datetime import datetime
from django.db.models import Count

def home(request):
    candidati = Candidato.objects.all()
    utenti_censiti = UtentiCensiti.objects.all()
    
    context = {
        "candidati": candidati
    }
    
    if request.method == 'POST':
        err_msg = ''
        p = Previsione()
        p.candidato = candidati.get(id=request.POST['candidato'])
        if utenti_censiti.filter(utente=request.POST['firma'].lower()).exists():
            utente = utenti_censiti.get(utente=request.POST['firma'].lower())
            if not Previsione.objects.filter(utente=utente).exists():
                p.utente = utente
            else:
                err_msg = "L'utente ha già votato"                
        else:
            err_msg = "Utente non censito"
            
        if not err_msg:
            p.data_prevista = datetime.now()
            p.save()
            context.update({
                'conf_msg': 'Votazione registrata!'
            })
        else:
            context.update({
                'err_msg': err_msg
            })
            
    previsioni = Previsione.objects.all().annotate(num_candidato=Count('candidato'))
    context.update({ "previsioni": previsioni })
    
    return render(request, "index.html", context=context)
