"""
Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

"""

nota_01 = float(input('Digite a primeira nota: '))
nota_02 = float(input('Digite a segunda nota: '))
nota_03 = float(input('Digite a terceira nota: '))

media = (nota_01 + nota_02 + nota_03) / 3

print(f'A média entre as notas {nota_01, nota_02, nota_03} é: {media:.2f}')