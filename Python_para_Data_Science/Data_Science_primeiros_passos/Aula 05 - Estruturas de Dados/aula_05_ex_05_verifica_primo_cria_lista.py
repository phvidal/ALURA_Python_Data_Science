"""
Faça um programa que, ao inserir um número qualquer, criará uma lista contendo todos os números primos entre 1 e o número digitado.

"""

number = int(input('Digite um número: '))
lista_num_primo = []

for i in range(2, number): #cria um laço que vai percorrer item por item até chegar no número inserido
    primo = True #define que a variável primo é verdadeira
    for j in range(2, i): #cria um novo laço que vai percorrer tudo que for maior de 2 até o 'i' e verifica se a divisão é igual a zero, se for, não é primo
        if i % j == 0: #itera o j de 2 até i e verifica se o resultado da zero, se não, j+=1.
            primo = False #se for igual a zero, não é primo
            break #encerro esse if
        
    if primo: #caso seja diferente de 0, apenda o valor de 'i' em lista de números primos
        lista_num_primo.append(i)

print(lista_num_primo)

