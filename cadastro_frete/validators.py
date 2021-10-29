import re
from validate_docbr import CNPJ

def cnpj_valido(numero_cnpj):
    cnpj = CNPJ
    return cnpj.validate(numero_cnpj)

def nome_valido(name):
        return name.isalpha()

def site_valido(self,site):
    '''verifica se o site é válido'''
    modelo = '(https//)*(\S{1,30}.com.br|\S{1,30}.com)'
    resp = re.findall(site, modelo)
    self.resposta = resp[0][0] + resp[0][1]
    return self.resposta