from django.shortcuts import render
from django.http import HttpResponse
from .models import Processo


def listar_processos(request): 
    processos = Processo.objects.all() 
    template = 'listar_processos.html'
    return render(request, template, {'processos': processos})