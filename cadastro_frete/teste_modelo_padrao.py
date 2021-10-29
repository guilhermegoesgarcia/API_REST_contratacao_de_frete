import re

modelo_0 = 'google.com.br'
modelo_1 = 'https//www.google.com.br'
modelo_2 = 'www.google.com'

modelo_geral ='(https//)*(\S{1,30}.com.br|\S{1,30}.com)'

resposta = re.findall(modelo_geral,modelo_0)

if resposta:
    teste = 'Verdadeiro'
else: teste ='Falso'

print(teste, resposta)