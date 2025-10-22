from django.shortcuts import render, redirect
from .forms import CandidatForm
from .models import Candidat

def inscription(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('succes')
    else:
        form = CandidatForm()
    return render(request, 'inscriptions/inscription.html', {'form': form})

def succes(request):
    return render(request, 'inscriptions/succes.html')
def accueil(request):
    return render(request, 'inscriptions/accueil.html')
def liste_candidats(request):
    candidats = Candidat.objects.all().order_by('-date_inscription')  # tri du plus récent au plus ancien
    return render(request, 'inscriptions/liste_candidats.html', {'candidats': candidats})

