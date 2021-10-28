from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from cadastro_frete.models import CadastroEmpresa, CadastroCliente, CadastroOferta, Lance
from cadastro_frete.serializer import *

# Create your views here.

class CadastroEmpresa_ViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os cadastros'''
    queryset = CadastroEmpresa.objects.all()
    serializer_class = CadastroEmpresa_Serializer

class CadastroCliente_ViewSet(viewsets.ModelViewSet):
    queryset = CadastroCliente.objects.all()
    serializer_class = CadastroCliente_Serializer

class CadastroOferta_ViewSet(viewsets.ModelViewSet):
    queryset = CadastroOferta_Serializer.objects.all()
    serializer_class = CadastroOferta_Serializer

class Lance_ViewSet(viewsets.ModelViewSet):
    queryset = Lance_Serializer.objects.all()
    serializer_class = Lance_Serializer

