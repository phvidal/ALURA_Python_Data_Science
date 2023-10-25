"""
Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00.
Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.

Dica: use a variável pi e o método pow() da biblioteca math. O cálculo de área de um círculo é de:  Area=π x r2

"""

from math import pi, pow

raio_cliente = float(input('Por favor, informe o raio da área que deseja instalar a grama: '))

valor_metro_quadrado = 25

area = pi*pow(raio_cliente, 2)
preco_final = area * valor_metro_quadrado

print(f'O valor a ser pago por {raio_cliente:.2f} metros quadrados é de {preco_final:.2f} reais')

