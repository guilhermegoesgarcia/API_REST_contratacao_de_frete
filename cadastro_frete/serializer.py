from rest_framework import serializers
from cadastro_frete.models import CadastroEmpresa,CadastroCliente,CadastroOferta,Lance

class CadastroEmpresa_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroEmpresa
        fields = '__all__'

class CadastroCliente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroCliente
        fields = '__all__'

class CadastroOferta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroOferta
        fields = '__all__'

class Lance_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lance
        fields = '__all__'