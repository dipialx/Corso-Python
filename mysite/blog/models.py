#blog/models.py
from django.db import models

class Autore(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome

class Articolo(models.Model):
    titolo = models.CharField(max_length=200)
    contenuto = models.TextField()
    pubblicato = models.DateField(auto_now_add=True)
    autore = models.ForeignKey(Autore, on_delete=models.SET_NULL, related_name="articoli", null=True)

    def __str__(self):
        return self.titolo
