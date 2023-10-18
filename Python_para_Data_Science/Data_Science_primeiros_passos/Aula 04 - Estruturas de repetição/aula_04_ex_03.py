"""
Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. 
Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. 
Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

"""

qtd_pessoas = 1
notas = ''

while qtd_pessoas <= 15:
  notas = int(input('Digite um valor entre 1 e 5: '))
  if notas < 0 or notas > 5:
    print('Digite um número válido!')
  else:
    print(f'A nota de avaliação do cliente {qtd_pessoas} foi: {notas}')
    qtd_pessoas += 1

# SOLUÇÃO ALURA
#for i in range(15):
#  nota = float(input(f'Insira a nota da pessoa usuária {i}: '))

  # verifica se a nota está entre 0 e 5
  # se estiver, o laço rodará ininterruptamente até ser obtido um valor válido
#  while (nota < 0) or (nota > 5):
#    nota = float(input(f'Nota inválida, insira novamente a nota da pessoa usuária {i}: '))

#print('Verificação feita. Todas as notas são válidas')