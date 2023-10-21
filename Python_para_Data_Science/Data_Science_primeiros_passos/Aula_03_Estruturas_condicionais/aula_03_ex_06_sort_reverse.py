"""
Escreva um programa que leia três números e os exiba em ordem decrescente.

"""
numero_01 = int(input('Digite um número: '))
numero_02 = int(input('Digite mais um número: '))
numero_03 = int(input('Digite mais um número: '))

numeros = [numero_01, numero_02, numero_03]

numeros.sort(reverse=True)
print(f'Números em ordem decrescente: {numeros}')

# https://docs.python.org/pt-br/dev/howto/sorting.html

# SOLUÇÃO ALURA
# # Coletamos os 3 números
# num1 = int(input('Informe o primeiro número: '))
# num2 = int(input('Informe o segundo número: '))
# num3 = int(input('Informe o terceiro número: '))

# # Comparação entre os 3 números
# if (num1 >= num2) and (num1 >= num3):
#     print(num1)
#     if num2 >= num3:
#         print(num2)
#         print(num3)
#     else:
#         print(num3)
#         print(num2)
# elif (num2 >= num1) and (num2 >= num3):
#     print(num2)
#     if num1 >= num3:
#         print(num1)
#         print(num3)
#     else:
#         print(num3)
#         print(num1)
# else:
#     print(num3)
#     if num1 >= num2:
#         print(num1)
#         print(num2)
#     else:
#         print(num2)
#         print(num1)