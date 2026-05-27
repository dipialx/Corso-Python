from rest_framework import serializers
from .models import Articolo

class ArticoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articolo
        fields = ["id", "titolo", "contenuto", "pubblicato", "autore"]
