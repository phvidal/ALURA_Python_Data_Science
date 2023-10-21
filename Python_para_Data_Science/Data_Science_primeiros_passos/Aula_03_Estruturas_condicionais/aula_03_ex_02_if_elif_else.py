"""
Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e 
informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

"""

variacao = float(input('Digite a variação de ganhos/perdas de sua empresa: '))

if variacao > 0:
    print(f'A sua empresa obteve um crescimento percentual de {variacao}%')
elif variacao < 0:
    print(f'A sua empresa obteve um decrescimento percentual de {variacao}%')
else:
    print(f'Sua empresa não teve lucro nem prejuízo.')