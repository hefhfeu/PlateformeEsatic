from django import forms
from .models import Candidat

class CandidatForm(forms.ModelForm):
    class Meta:
        model = Candidat
        fields = [
            'nom',
            'prenom',
            'niveau_etudes',
            'etablissement_origine',
            'concours_souhaite',
            'extrait_naissance',
            'certificat',
            'lettre_motivation',
            'diplome',
            'photo',
        ]