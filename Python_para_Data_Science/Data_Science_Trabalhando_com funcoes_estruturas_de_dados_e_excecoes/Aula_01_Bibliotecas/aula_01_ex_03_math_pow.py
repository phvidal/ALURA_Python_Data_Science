"""
Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

"""
from math import pow

x = int(input('Digite um número que será a base de sua operação: '))
y = int(input('Digite um número que elevará o primeiro a essa potência: '))

print(f'{x} elevado a {y} é: {pow(x, y):.0f}')