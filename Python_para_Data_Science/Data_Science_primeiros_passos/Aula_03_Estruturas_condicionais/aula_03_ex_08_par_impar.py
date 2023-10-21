"""
Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

"""

numero_usuario = int(input('Digite um número: '))
validacao = numero_usuario % 2

if validacao == 0:
    print(f'O número {numero_usuario} é par')
else:
    print(f'O número {numero_usuario} é ímpar')