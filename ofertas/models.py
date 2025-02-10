from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=500)
    imagem_url = models.URLField(max_length=500)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    preco_sem_desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentual_desconto = models.IntegerField(null=True, blank=True)
    parcelamento = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(max_length=500)
    tipo_entrega = models.CharField(max_length=50, choices=[('Full', 'Full'), ('Normal', 'Normal')])
    frete_gratis = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
