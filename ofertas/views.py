from django.shortcuts import render
from .models import Produto


def ofertas(request):
    produtos = Produto.objects.all()
    return render(request, 'ofertas/ofertas.html', {'produtos': produtos})
