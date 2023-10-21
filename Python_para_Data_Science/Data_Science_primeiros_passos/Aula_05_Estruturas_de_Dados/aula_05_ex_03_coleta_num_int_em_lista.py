"""
Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].

"""
lista_usr = []
cont = 1

while cont <= 5:
    lista_usr.append(int(input('Digite um número: ')))
    cont += 1

print(f'Esses são os números de sua lista: {lista_usr}')

# SOLUÇÃO ALURA:

# # Lista que irá armazenar os 5 números inteiros
# lista_numeros = []

# # Criamos um laço que vai iterar 5 vezes para receber os 5 números
# for i in range(0, 5):
#   # Coletamos o valor e inserimos na lista por 5 vezes
#   numero = int(input('Digite um número inteiro: '))
#   lista_numeros.append(numero)
# #Resultado
# print(f'Lista de números inseridos: {lista_numeros}')