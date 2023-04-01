from django.db import models
# Create your models here.

#Modelo tabela pokemon
class Pokemon(models.Model):
    name = models.CharField(max_length=20)
    types = models.CharField(max_length=200)
    class Meta:
        db_table = 'pokemon'

#Modelo tabela tipos
class PokemonTypes(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        db_table = 'pokemon_types'