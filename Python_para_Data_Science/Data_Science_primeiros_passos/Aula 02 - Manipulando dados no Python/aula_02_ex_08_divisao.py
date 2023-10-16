"""
Crie um programa que solicite dois valores numéricos, um numerador e um denominador,
e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

"""
numerador = int(input('Digite um número: '))
denominador = int(input('Digite mais um número (não pode ser o número ZERO): '))

divisao = numerador / denominador

print(f'A divisão entre {numerador} e {denominador} é: {divisao}')