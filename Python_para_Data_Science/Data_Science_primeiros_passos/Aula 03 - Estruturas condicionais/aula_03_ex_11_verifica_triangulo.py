"""
Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. 
O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, 
se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

"""


lado_a = int(input('Digite um número que representa um dos lados de um triângulo: '))
lado_b = int(input('Digite um número que representa mais um dos lados de um triângulo: '))
lado_c = int(input('Digite um número que representa o último lado de um triângulo: '))

equilatero = lado_a == lado_b and lado_b == lado_c
isosceles = lado_a == lado_b or lado_b == lado_c or lado_c == lado_a
escaleno = lado_a != lado_b and lado_b != lado_c and lado_c != lado_a

if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    print('Isso um triângulo!')
    if equilatero:
        print('É um triângulo Equilátero!')
    elif isosceles:
        print('É um triângulo Isósceles!')
    elif escaleno:
        print('É um triângulo Escaleno!')
else:
    print('Não é um triângulo.')


# RESOLUÇÃO ALURA:
# # Coletamos os lados de um triângulo
# print('Coletaremos os lados de um triângulo.')
# lado1 = float(input('Digite o comprimento do primeiro lado: '))
# lado2 = float(input('Digite o comprimento do segundo lado: '))
# lado3 = float(input('Digite o comprimento do terceiro lado: '))

# # Verificamos de os lados formam um triângulo
# if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
#     print('Os valores podem formar um triângulo!')
#     # comparamos os lados para verificar o tipo de triângulo
#     if (lado1 == lado2) and (lado2 == lado3):
#         print('O triângulo é equilátero.')
#     elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
#         print('O triângulo é escaleno.')
#     else:
#         print('O triângulo é isósceles.')
# else:
#     print('Os valores não podem formar um triângulo!')