from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArticoloSerializer

# Create your views here.
from .models import Articolo

def lista_articoli(request):
    articoli = Articolo.objects.all()
    return render(request, "blog/lista.html", {"articoli": articoli})


class ArticoloViewSet(viewsets.ModelViewSet):
    queryset = Articolo.objects.all()
    serializer_class = ArticoloSerializer
