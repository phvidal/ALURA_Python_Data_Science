"""
Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

    [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

Utilize o return na função e salve a nova lista na variável mult_3.

"""

def multiplos_3(lista):
    mult_3 = []

    for i in lista:
        if i % 3 == 0:
            mult_3.append(i)
        else:
            continue
    return mult_3

lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
resultado = multiplos_3(lista)
print(resultado)

