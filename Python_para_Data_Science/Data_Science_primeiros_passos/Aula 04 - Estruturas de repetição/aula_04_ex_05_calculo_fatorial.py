"""
Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. 
O fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. 
Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

"""

num_usuario = int(input('Digite o um número de 1 a 20: '))

contador = num_usuario
fatorial = 1

while contador > 0:
  fatorial *= contador
  contador -= 1

print(f'O fatorial de {num_usuario} é {fatorial}')