'''
Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. 
Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a 
distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. 
Encerre a entrada de dados com um número negativo.

'''

idade_cliente = int(input('Digite a idade do cliente (ou um número negativo para encerrar): '))

idade_0_25 = 0
idade_26_50 = 0
idade_51_75 = 0
idade_76_100 = 0

while idade_cliente > 0:
    if idade_cliente >= 0 and idade_cliente <= 25:
        idade_0_25 += 1
    elif idade_cliente >= 26 and idade_cliente <= 50:
        idade_26_50 += 1
    elif idade_cliente >= 51 and idade_cliente <= 75:
        idade_51_75 += 1
    elif idade_cliente >= 76 and idade_cliente <= 100:
        idade_76_100 += 1
    else:
        print('Você não digitou um valor acima de 100, não será contabilizado!')
        
    idade_cliente = int(input('Digite a idade do cliente (ou um número negativo para encerrar): '))

print(f'Tivemos um total de {idade_0_25} clientes entre 0 e 25 anos')
print(f'Tivemos um total de {idade_26_50} clientes entre 26 e 50 anos')
print(f'Tivemos um total de {idade_51_75} clientes entre 51 e 75 anos')
print(f'Tivemos um total de {idade_76_100} clientes entre 76 e 100 anos')