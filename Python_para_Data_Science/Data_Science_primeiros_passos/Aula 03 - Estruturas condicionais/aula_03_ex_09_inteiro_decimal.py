"""
Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

"""
num = float(input('Digite um número inteiro: '))

if num % 1 == 0:
  print('É um número inteiro')
else:
  print('É um número decimal')