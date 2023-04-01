from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics

from .models import *
from .serializers import *

class PokemonsView(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypesView(viewsets.ModelViewSet):
    queryset = PokemonTypes.objects.all()
    serializer_class = PokemonTypeSerializer  

#RELACIONAMENTO ENTRE POKEMONS E TIPOS
class PokemonTypesView(generics.ListAPIView):
    serializer_class = PokemonSerializer
    def get_queryset(self):        
        id = self.kwargs['id']
        return Pokemon.objects.filter(types__contains=id)