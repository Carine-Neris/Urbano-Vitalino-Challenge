import csv, io
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from processos.models import Processo 


def profile_upload(request):
    template = "processo_cadastrar.html"

    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']
    
    data_set = csv_file.read().decode('UTF-8')
   
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=';'):
        _, created = Processo.objects.update_or_create(
            pasta = column[0],
            comarca = column[1],
            uf = column[2]
        )
    context = {}
    return render(request, template, context)
