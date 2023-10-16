"""
Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite")
e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

"""

turma = input('Qual turma você estuda? (Manhã, Tarde ou Noite): ').title()

if turma == 'Manhã':
    print('Bom dia!')
elif turma == 'Tarde':
    print('Bom tarde!')
elif turma == 'Noite':
    print('Boa noite!')
else:
    print('Valor inválido')