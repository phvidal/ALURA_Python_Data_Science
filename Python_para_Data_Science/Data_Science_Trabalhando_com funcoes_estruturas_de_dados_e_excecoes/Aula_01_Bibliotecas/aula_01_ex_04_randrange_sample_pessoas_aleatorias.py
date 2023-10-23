"""
Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. 
A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes.

Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.

"""

from random import randrange, sample

numero_pessoas_sorteio = int(input('Digite quantas pessoas irão participar do sorteio, cada uma receberá um código: '))

codigos_pessoas = []

for i in range(0, numero_pessoas_sorteio):
    codigos_pessoas.append(randrange(100))

print(f'Esses são os códigos dos {numero_pessoas_sorteio} participantes: \n{codigos_pessoas}\n')

print(f'O código sorteado foi: {sample(codigos_pessoas, 1)}')

# SOLUÇÃO ALURA
# from random import randint
# # Transformando a quantidade de participantes de string para inteiro
# n = int(input("Digite o nº de participantes do sorteio: "))
# # Sorteando um número no intervalo de 1 até a quantidade de participantes
# print(f"O número sorteado foi {randint(1, n)}")
