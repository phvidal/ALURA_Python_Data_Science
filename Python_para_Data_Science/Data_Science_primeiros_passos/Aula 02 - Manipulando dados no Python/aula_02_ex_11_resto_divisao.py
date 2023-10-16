"""
Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. 
Deixe claro que o valor do denominador não pode ser 0.

"""

numerador = int(input('Digite o valor do numerador: '))
denominador = int(input('Digite o valor do denominador "O valor não pode ser ZERO".: '))

resto_divisao = numerador % denominador

print(f'O resto da divisão entre {numerador} e {denominador} é: {resto_divisao}')