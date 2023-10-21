"""

Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. 
Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. 
Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. 
Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. 
Tenha em mente algumas dicas:

O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.

"""

quantidade = float(input('Quantos livros você deseja abastecer?: '))
combustivel = input('Qual combustível você escolhe? Etanol [E] ou Diesel [D]: ').upper()

lt_etanol = 1.7
lt_diesel = 2.0

if combustivel == 'E' and quantidade <= 15.0:
  valor_desc = lt_etanol - (lt_etanol / 100)*2
  valor_real = quantidade * valor_desc
  print((f'Você irá pagar {valor_real:.2f} reais para abastecer!').replace('.', ','))
elif combustivel == 'E' and quantidade > 15:
  valor_desc = lt_etanol - (lt_etanol / 100)*4
  valor_real = quantidade * valor_desc
  print((f'Você irá pagar {valor_real:.2f} reais para abastecer!').replace('.', ','))
elif combustivel == 'D' and quantidade <= 15.0:
  valor_desc = lt_diesel - (lt_diesel / 100)*3
  valor_real = quantidade * valor_desc
  print((f'Você irá pagar {valor_real:.2f} reais para abastecer!').replace('.', ','))
elif combustivel == 'D' and quantidade > 15.0:
  valor_desc = lt_diesel - (lt_diesel / 100)*5
  valor_real = quantidade * valor_desc
  print((f'Você irá pagar {valor_real:.2f} reais para abastecer!').replace('.', ','))
else:
  print('Você escolheu uma opção de combustível inexistente, apete D para Diesel ou E para Etanol')