from rest_framework import routers
from .views import *
from django.urls import path

router = routers.DefaultRouter()
router.register(r'pokemons', PokemonsView)
router.register(r'types', TypesView)
urlpatterns = [
    path('pokemons/types/<id>/', PokemonTypesView.as_view()),
]
urlpatterns += router.urls