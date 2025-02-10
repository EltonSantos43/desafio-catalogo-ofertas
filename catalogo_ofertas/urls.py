from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ofertas.urls')),  # Incluindo as rotas do app "ofertas"
]
