"""
Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

"""

prod_01 = float(input('Valor do primeiro produto: '))
prod_02 = float(input('Valor do segundo produto: '))
prod_03 = float(input('Valor do terceiro produto: '))

mais_barato = prod_01

if prod_02 < mais_barato:
    mais_barato = prod_02
if prod_03 < mais_barato:
    mais_barato = prod_03


print(f'O produto mais barato é o de valor: {mais_barato}')