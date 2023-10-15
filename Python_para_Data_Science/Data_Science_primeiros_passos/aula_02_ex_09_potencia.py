"""
Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.

"""

operador = int(input('Digite um número: '))
potencia = int(input('Digite mais um número: '))

exponenciacao = operador ** potencia

print(f'A a exponenciação entre {operador} e {potencia} é: {exponenciacao}')