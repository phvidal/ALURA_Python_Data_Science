"""
Você recebeu uma demanda para gerar números de token para o acesso ao aplicativo de uma empresa. 
O token precisa ser par e variar de 1000 até 9998. 
Escreva um código que solicita à pessoa usuária o seu nome e gera uma mensagem junto a esse token gerado aleatoriamente:

"Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

"""
nome = input('Qual é o seu nome?: ')

from random import randrange

token = randrange(1000, 10000, 2)

print(f'Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!')

