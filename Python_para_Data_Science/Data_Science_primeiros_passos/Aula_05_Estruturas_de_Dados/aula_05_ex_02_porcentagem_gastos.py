"""
Com os mesmos dados da questão anterior, defina quantas compras foram acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

Lista anterior:
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

"""

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
gasto_acima_3000 = 0
total_gastos = len(gastos)

for gasto in gastos:
    if gasto > 3000:
        gasto_acima_3000 += 1

porcentagem_acima_3000 = (gasto_acima_3000 / total_gastos) * 100

print(f'Houveram {gasto_acima_3000} gastos acima dos R$3.000,00')
print(f'Os gastos acima de R$3.000,00 representam {porcentagem_acima_3000:.2f}% do total de gastos')



