from django.urls import path
import datetime
from .views import profile_upload


app_name='cadastro_processos'


urlpatterns = [
    path('processo/cadastro/',profile_upload, name='cadastro_processo'),
]