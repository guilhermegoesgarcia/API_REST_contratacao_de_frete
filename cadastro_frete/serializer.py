from rest_framework import serializers
from cadastro_frete.models import CadastroEmpresa,CadastroCliente,CadastroOferta,Lance

class CadastroEmpresa_Serializer(serializers.ModelSerializer):
    class meta:
        model = CadastroEmpresa
        fields = '__all__'

class CadastroCliente_Serializer(serializers.ModelSerializer):
    class meta:
        model = CadastroCliente
        fields = '__all__'

class CadastroOferta_Serializer(serializers.ModelSerializer):
    class meta:
        model = CadastroOferta
        fields = '__all__'

class Lance_Serializer(serializers.ModelSerializer):
    class meta:
        model = Lance
        fields = '__all__'