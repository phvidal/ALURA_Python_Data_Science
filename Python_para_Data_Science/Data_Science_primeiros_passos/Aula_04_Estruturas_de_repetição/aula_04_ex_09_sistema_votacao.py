'''
Em uma eleição para gerência em uma empresa com 20 funcionários, existem quatro candidatos. Escreva um programa que calcule o vencedor da eleição. 
A votação ocorreu da seguinte maneira:

    Cada funcionário votou em um dos quatro candidatos (representados pelos números 1, 2, 3 e 4).
    Também foram contabilizados os votos nulos (representado pelo número 5) e os votos em branco (representado pelo número 6).

Ao final da votação, o programa deve exibir o total de votos para cada candidato, o número de votos nulos e o número de votos em branco. 
Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

'''

voto = int(input('Seu voto vai para o candidato: 1, 2, 3, 4 ou 5 para anular e 6 para votar em branco?: '))

candidato_01 = 0
candidato_02 = 0
candidato_03 = 0
candidato_04 = 0
nulo = 0
branco = 0

funcionarios = 0

while funcionarios <= 20:
    if voto == 1:
        candidato_01 += 1
        funcionarios += 1
    elif voto == 2:
        candidato_02 += 1
        funcionarios += 1
    elif voto == 3:
        candidato_03 += 1
        funcionarios += 1
    elif voto == 4:
        candidato_04 += 1
        funcionarios += 1
    elif voto == 5:
        nulo += 1
        funcionarios += 1
    elif voto == 6:
        branco += 1
        funcionarios += 1
    else:
        print('Seu voto não é valido!')

    voto = int(input('Seu voto vai para o candidato: 1, 2, 3, 4 ou 5 para anular e 6 para votar em branco?: '))

porcentagem_votos_nulo = (nulo / funcionarios) * 100
porcentagem_votos_branco = (branco / funcionarios) * 100

print(f'Candidato 1 teve: {candidato_01} votos')
print(f'Candidato 2 teve: {candidato_02} votos')
print(f'Candidato 3 teve: {candidato_03} votos')
print(f'Candidato 4 teve: {candidato_04} votos')
print(f'Foram {nulo} votos nulos')
print(f'Foram {branco} votos brancos')
print(f'Percentual de votos nulos: {porcentagem_votos_nulo:.2f}%')
print(f'Percentual de votos brancos: {porcentagem_votos_branco:.2f}%')





    



