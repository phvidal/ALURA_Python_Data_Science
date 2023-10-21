"""
Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. 
Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:

"""

numero_tabuada = int(input('Você gostaria de ver a tabuada de qual número?: '))

index = 1

while index <= 10:
  print(f'{numero_tabuada} x {index} = {numero_tabuada * index}')
  index += 1