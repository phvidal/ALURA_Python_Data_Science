"""
Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

validacao = n1 > n2

if validacao:
    print(f'O número {n1} é maior que o {n2}')
else:
    print(f'O número {n2} é maior que o {n1}')