from rest_framework import serializers
from .models import *

#Serialize modelo pokemon
class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'types']

#Serialize modelo tipos
class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonTypes
        fields = ['id', 'name']             
