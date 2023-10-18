'''
Os números primos possuem várias aplicações dentro da Ciência de Dados, por exemplo,
na criptografia e segurança. Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

'''

# numero_usr = int(input('Digite um número: '))

# if numero_usr <= 1:
#     print(f'O número {numero_usr} não é um número primo')
# else:
#     for i in range(2, numero_usr):
#         if numero_usr % i == 0:
#             print(f'O número {numero_usr} não é um número primo')
#             break
#         else:
#             print(f'O número {numero_usr} é primo!')
#             break


#coletamos o número
num = int(input('Insira um número inteiro: '))

# números inteiros iguais ou abaixo de 1 não consideramos primos
if num > 1:
    for i in range(2, num):
        # verificamos todos os restos de divisões entre todos os números abaixo de num
        # se algum resto for 0, então ele é divisível por outro número além dele e 1
        if (num % i) == 0:
            print(f'{num} não é um número primo')
            break
    else:
        print(f'{num} é um número primo')
else:
    print(f'{num} não é um número primo')