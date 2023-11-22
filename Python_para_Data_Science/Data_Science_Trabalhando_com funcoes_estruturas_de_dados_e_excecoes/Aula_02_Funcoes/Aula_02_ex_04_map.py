"""
Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

"""

lista_usr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = lambda x: x ** 2
lista_quadrado = list(map(quadrado, lista_usr)) # o exercício acaba aqui

#realizei alguns teste para entender qual era o tipo do dado list(map())

teste = list(lista_quadrado)

print(f'Esse é o quadrado: {quadrado}')
print(type(f'Esse é o tipo do quadrado: {quadrado}'))

print(f'Esse é a lista_quadrado: {lista_quadrado}')
print(type(f'Esse é o tipo da lista_quadrado: {lista_quadrado}'))
print(teste)
print(type(teste))

