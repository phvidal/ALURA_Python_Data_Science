"""
Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. 
Deixe claro que o valor do denominador não pode ser 0.

"""

numerador = int(input('Digite o valor do numerador: '))
denominador = int(input('Digite o valor do denominador "O valor não pode ser ZERO".: '))

divisao_inteira = numerador // denominador

print(f'A divisão inteira entre {numerador} e {denominador} é: {divisao_inteira}')