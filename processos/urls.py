from django.urls import path
from .views import listar_processos


app_name = 'processos'


urlpatterns = [
    path('processos/listar/',listar_processos, name='processos')
]