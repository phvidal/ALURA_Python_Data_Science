"""
Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

"""

n1 = 5
n2 = 12
n3 = 20
n4 = 15

p1 = 1
p2 = 2
p3 = 3
p4 = 4

media_ponderada_numeros = n1*p1 + n2*p2 + n3*p3 + n4*p4
media_ponderada_pesos = p1 + p2 + p3 + p4

media_ponderada = media_ponderada_numeros / media_ponderada_pesos

print(f'A média ponderada entre os números {n1, n2, n3, n4} e os pesos {p1, p2, p3, p4} é: {media_ponderada}')