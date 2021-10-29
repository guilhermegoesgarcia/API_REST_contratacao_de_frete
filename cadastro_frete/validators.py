import re
from validate_docbr import CNPJ

def cnpj_valido(numero_cnpj):
    cnpj = CNPJ()
    return cnpj.validate(numero_cnpj)

def nome_valido(name):
        return name.isalpha()

def site_valido(site):
    '''verifica se o site é válido'''
    modelo = '(https//)*(\S{1,30}.com.br|\S{1,30}.com)'
    resposta = re.findall(modelo,site)
    return resposta

