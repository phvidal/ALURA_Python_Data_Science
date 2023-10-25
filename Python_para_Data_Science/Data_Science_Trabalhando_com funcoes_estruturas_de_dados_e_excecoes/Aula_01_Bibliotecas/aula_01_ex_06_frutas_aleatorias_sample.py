"""
Para diversificar e atrair novos clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". 
Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 frutas para compor a salada de frutas da pessoa cliente.

Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

"""

from random import sample #com essa biblioteca os valores escolhidos não se repetirão, se usasse o 'choices' poderia sair 3 vezes a maçã por exemplo!

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

salada_aleatoria = sample(frutas, k=3)

print(f'Sua salada será com as respectivas frutas: {salada_aleatoria[0]}, {salada_aleatoria[1]}, {salada_aleatoria[2]}!')


# from random import choices

# # Lista das frutas disponíveis
# frutas = ["maçã", "banana", "uva", "pêra","manga", "coco", 
#           "melancia", "mamão", "laranja", "abacaxi", "kiwi", "ameixa"]

# # Gerando uma lista com a escolha aleatoria de 3 frutas 
# salada = choices(frutas, k=3)

# # Imprimindo os itens da lista de frutas gerada
# print(f"A salada surpresa é: {salada[0]}, {salada[1]} e {salada[2]}")



