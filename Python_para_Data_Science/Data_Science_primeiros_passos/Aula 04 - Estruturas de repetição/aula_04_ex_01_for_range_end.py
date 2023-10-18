"""
Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

"""
num_01 = int(input('Digite um número: '))
num_02 = int(input('Digite um número: '))

# Se o primeiro número for maior que o segundo, precisamos inverter a ordem, para começarmos a contar do mais
# baixo para o mais alto
if num_01 > num_02:
    num_01, num_02 = num_02, num_01

print(f'Os números inteiros entre {num_01} e {num_02} são:')

for i in range(num_01, num_02 + 1):
    print(i, end=' ')