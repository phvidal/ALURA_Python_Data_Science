"""
Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. 
O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. 
A partir do valor da variação, deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para bonificações abaixo de -10%: corte de gastos.

"""

ano_01 = float(input('Digite o valor de vendas do ano de 2022: '))
ano_02 = float(input('Digite o valor de vendas do anos de 2023: '))

valor_variacao = ano_02 - ano_01
porcentagem = (valor_variacao / ano_01) * 100

# print(valor_variacao)
# print(f'{porcentagem:.2f}')

if porcentagem >= 20:
    print(f'Nossas vendas subiram {porcentagem:.2f}%. Bonificação para o time de vendas!')
elif porcentagem == 2 and porcentagem < 20:
    print(f'Nossas vendas subiram {porcentagem:.2f}%. Pequena bonificação para o time de vendas!')
elif porcentagem < 2 and porcentagem > -10:
    print(f'Nossas vendas tiveram uma variação de {porcentagem:.2f}%. Teremos políticas de incentivo às vendas!')
else:
    print(f'Nossas vendas tiveram uma queda de {porcentagem:.2f}%. Teremos cortes de gastos!')

    
