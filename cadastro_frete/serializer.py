from rest_framework import serializers
from cadastro_frete.models import CadastroEmpresa,CadastroCliente,CadastroOferta,Lance
from cadastro_frete.validators import *

class CadastroEmpresa_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroEmpresa
        fields = '__all__'
    def validate(self, data):
        if not cnpj_valido(data['doc']):
            raise serializers.ValidationError({'doc': "Número de CNPJ inválido"})
        if not site_valido(data['site']):
            raise serializers.ValidationError({'site': "Endereço de SITE inválido"})
        return data

class CadastroCliente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroCliente
        fields = '__all__'
    def validate(self, data):
        if not cnpj_valido(data['doc']):
            raise serializers.ValidationError({'doc': "Número de CNPJ inválido"})
        if not site_valido(data['site']):
            raise serializers.ValidationError({'site': "Endereço de SITE inválido"})
        return data

class CadastroOferta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroOferta
        fields = '__all__'

class Lance_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lance
        fields = '__all__'