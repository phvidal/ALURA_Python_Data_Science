"""
Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

"""

lista_usr = []
cont = 1

while cont <= 5:
    lista_usr.append(int(input('Digite um número: ')))
    cont += 1


print(f'Esses são os números de sua lista: {lista_usr[::-1]}')