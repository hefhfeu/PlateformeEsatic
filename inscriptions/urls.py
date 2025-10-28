from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscription, name='inscription'),
    path('succes/', views.succes, name='succes'),
    path('liste/', views.liste_candidats, name='liste_candidats'),  # ✅ nouvelle route
]