"""
Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e faça uma análise. 
Portanto, escreva um programa que leia temperaturas e informe a média delas. 
A leitura deve ser encerrada ao ser enviado o valor -273°C.

"""

temperatura = float(input('Insira uma temperatura em Celsius: '))

contador = 0
soma = 0

while temperatura != -273:
  soma += temperatura
  contador += 1
  temperatura = float(input('Insira uma temperatura em Celsius: '))

media = soma / contador

print(f'A média das temperaturas é de {media:.2f} graus Celsius')