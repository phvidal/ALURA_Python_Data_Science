"""
Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. 
O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

"""

num01 = float(input('Digite um número: '))
num02 = float(input('Digite mais um número: '))
operacao = input('Escolha uma operação aritmética (subtração, adição, multiplicação ou divisão): ').lower()

subtracao = num01 - num02
adicao = num01 + num02
multiplicacao = num01 * num02
divisao = num01 / num02

if operacao in 'subtração, subtracao, subtraçao, subtracão':
  print(f'O resultado dessa subtração é: {subtracao} ')
  if subtracao % 2 == 0:
    print('Esse resultado é um número par')
  else:
    print('Esse resultado é um número impar')

  if subtracao >= 0:
    print('Esse resultado é positivo')
  else:
    print('Esse resultado é negativo')

  if subtracao % 1 == 0:
    print('Esse resultado é um número inteiro')
  else:
    print('Esse resultado é um número decimal')

elif operacao in 'adicao, adição, adiçao, adicão':
  print(f'O resultado dessa adição é: {adicao}')

  if adicao % 2 == 0:
    print('Esse resultado é um número par')
  else:
    print('Esse resultado é um número impar')

  if adicao >= 0:
    print('Esse resultado é positivo')
  else:
    print('Esse resultado é negativo')

  if adicao % 1 == 0:
    print('Esse resultado é um número inteiro')
  else:
    print('Esse resultado é um número decimal')

elif operacao in 'multiplicação, multiplicacão, multiplicaçao, multiplicacao':
  print(f'O resultado dessa multiplicação é: {multiplicacao}')

  if multiplicacao % 2 == 0:
    print('Esse resultado é um número par')
  else:
    print('Esse resultado é um número impar')

  if multiplicacao >= 0:
    print('Esse resultado é positivo')
  else:
    print('Esse resultado é negativo')

  if multiplicacao % 1 == 0:
    print('Esse resultado é um número inteiro')
  else:
    print('Esse resultado é um número decimal')

elif operacao in 'divisao, divisão':
  print(f'O resultado dessa divisão é: {divisao}')

  if divisao % 2 == 0:
    print('Esse resultado é um número par')
  else:
    print('Esse resultado é um número impar')

  if divisao >= 0:
    print('Esse resultado é positivo')
  else:
    print('Esse resultado é negativo')

  if divisao % 1 == 0:
    print('Esse resultado é um número inteiro')
  else:
    print('Esse resultado é um número decimal')

else:
  print('Você escolheu uma operação inválida!!!')

# RESOLUÇÃO ALURA

# # Coletamos os números a serem operados e solicitamos a operação desejada pela pessoa usuária
# num1 = float(input('Informe o primeiro número: '))
# num2 = float(input('Informe o segundo número: '))
# operacao = input('Informe a operação desejada (+, -, *, /): ')

# # Verificamos o operador que foi selecionado e executa a operação matemática conforme a seleção
# if operacao == '+':
#     resultado = num1 + num2
# elif operacao == '-':
#     resultado = num1 - num2
# elif operacao == '*':
#     resultado = num1 * num2
# elif operacao == '/':
#     resultado = num1 / num2
# else: # Especificamos um resultado caso a pessoa usuária não digite alguma das operações corretamente.
#     print('Operação inválida, resultado da operação será 0')
#     resultado = 0 

# #  Fazemos as mesmas verificações das questões anteriores para fazer o relatório do cálculo entre números
# if resultado % 1 == 0:
#     print('O resultado é inteiro.')
# else:
#     print('O resultado é decimal.')

# if resultado > 0:
#     print('O resultado é positivo.')
# else:
#     print('O resultado é negativo.')

# if resultado % 2 == 0:
#     print('O resultado é par.')
# else:
#     print('O resultado é ímpar.')