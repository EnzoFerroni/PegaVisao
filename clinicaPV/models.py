from django.db import models

class Servicos(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f"Servico [nome={self.nome}]"
    