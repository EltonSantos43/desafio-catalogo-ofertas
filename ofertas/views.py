from django.shortcuts import render
from .models import Produto
from .scraper import scrape

def ofertas(request):
    produtos = Produto.objects.all()
    return render(request, 'ofertas/ofertas.html', {'produtos': produtos})

def atualizar_ofertas(request):
    scrape()  # Chama a raspagem
    produtos = Produto.objects.all()
    return render(request, 'ofertas/ofertas.html', {'produtos': produtos, 'atualizado': True})
