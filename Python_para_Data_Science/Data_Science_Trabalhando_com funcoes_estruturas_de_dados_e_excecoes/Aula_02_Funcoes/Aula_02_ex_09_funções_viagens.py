"""
Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. 
O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, 
crie três funções nas quais a 1ª calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e 
alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.

"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"

"""

dias = int(input('Quantos dias você vai passar na cidade?: '))
cidade = input('Para qual cidade você deseja viajar?[Salvador, Fortaleza, Natal e Aracaju]: ').title()
distancia = [850, 800, 300, 550]
passeios_alimentacao_dia = [200, 400, 250, 300]
km_litro = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(cidade):
    if cidade == 'Salvador':
        return (distancia[0] * 2 * gasolina / km_litro)
    elif cidade == 'Fortaleza':
        return (distancia[1] * 2 * gasolina / km_litro)
    elif cidade == 'Natal':
        return (distancia[2] * 2 * gasolina / km_litro)
    elif cidade == 'Aracaju':
        return (distancia[3] * 2 * gasolina / km_litro)
    
def gasto_passeio(cidade, dias):
    if cidade=="Salvador":
        return passeios_alimentacao_dia[0] * dias
    elif cidade=="Fortaleza":
        return passeios_alimentacao_dia[1] * dias
    elif cidade=="Natal":
        return passeios_alimentacao_dia[2] * dias 
    elif cidade=="Aracaju":
        return passeios_alimentacao_dia[3] * dias 
    
gasto_total = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {gasto_total:.2f} reais")
