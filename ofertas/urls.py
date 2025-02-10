from django.urls import path
from .views import ofertas, atualizar_ofertas

urlpatterns = [
    path('', ofertas, name="ofertas"),
    path('atualizar/', atualizar_ofertas, name="atualizar_ofertas"),
]
