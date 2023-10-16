"""
Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos 
consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

"""

valor_carro_01 = float(input('Digite o valor do carro no primeiro ano: '))
valor_carro_02 = float(input('Digite o valor do carro no segundo ano: '))
valor_carro_03 = float(input('Digite o valor do carro no terceiro ano: '))

valor_alto = valor_carro_01

if valor_carro_02 > valor_alto and valor_carro_02 > valor_carro_03:
    print(f'O valor mais alto é o {valor_carro_02} correspondente ao segundo ano.')
elif valor_carro_03 > valor_alto and valor_carro_03 > valor_carro_02:
    print(f'O valor mais alto é o {valor_carro_03} correspondente ao terceiro ano.')
else:
    print(f'O valor mais alto é o {valor_carro_01} correspondente ao primeiro ano.')


valor_baixo = valor_carro_01

if valor_carro_02 < valor_baixo and valor_carro_02 < valor_carro_03:
    print(f'O valor mais baixo é o {valor_carro_02} correspondente ao segundo ano.')
elif valor_carro_03 < valor_baixo and valor_carro_03 < valor_carro_02:
    print(f'O valor mais baixo é o {valor_carro_03} correspondente ao terceiro ano.')
else:
    print(f'O valor mais baixo é o {valor_carro_01} correspondente ao primeiro ano.')