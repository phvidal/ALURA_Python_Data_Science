"""
Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

"""
from random import choice

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

numero_aleatorio = choice(lista)
print(f'O número {numero_aleatorio} foi escolhido aleatoriamente da lista acima!')