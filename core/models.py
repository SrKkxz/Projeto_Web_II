from django.db import models

class Missao(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    xp_recompensa = models.IntegerField(default=10)
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo