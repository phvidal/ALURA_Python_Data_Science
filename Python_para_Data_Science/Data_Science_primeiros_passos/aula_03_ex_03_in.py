"""
Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

"""

letra = input('Insira uma letra: ')

vogais = 'a, e, i, o, u, A, E, I, O, U'

if letra in vogais:
    print(f'A letra {letra} é uma vogal!')
else:
    print(f'A letra {letra} é uma consoante!')