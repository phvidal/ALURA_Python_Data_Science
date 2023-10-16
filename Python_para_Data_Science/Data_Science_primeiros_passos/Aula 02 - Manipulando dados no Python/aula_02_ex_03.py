"""
Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima 
“Olá, [nome], você tem [idade] anos e mede [altura] metros!”.

"""

nome = input('Digite seu nome: ')
idade = int(input('Qual sua idade?: '))
altura = float(input('Qual sua altura?: ').replace(',', '.'))

print(f'Olá, {nome}, você tem {idade} anos e mede {altura} metros!')

