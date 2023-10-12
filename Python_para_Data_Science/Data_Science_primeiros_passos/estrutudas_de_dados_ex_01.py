litros = float(input('Quantos litros deseja abastecer?: '))
combustivel = input('Qual combustível deseja abastecer? [A] para álcool [G] gasolina: ').upper()


valor_gasolina = 5.39
valor_alcool = 4.89

if combustivel == 'A':
    if litros < 20:
        desconto = 0.03
        valor_total = litros * (valor_alcool - (valor_alcool * desconto))
        print(f'O valor a ser pago é {valor_total}')
    else:
        desconto = 0.05
        valor_total = litros * (valor_alcool - (valor_alcool * desconto))
        print(f'O valor a ser pago é {valor_total}')
elif combustivel == 'G':
    if litros < 20:
        desconto = 0.03
        valor_total = litros * (valor_gasolina - (valor_gasolina * desconto))
        print(f'O valor a ser pago é {valor_total}')
    else:
        desconto = 0.05
        valor_total = litros * (valor_gasolina - (valor_gasolina * desconto))
        print(f'O valor a ser pago é {valor_total}')
else:
    print('O combustível selecionado é inválido')


