"""
Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. 
Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

Tabuada do 7:
7 x 0 = 0
7 x 1 = 7
[...]
7 x 10 = 70
"""

def tabuada(number: int=[1]):
    contador = 0
    while contador <= 10:
        print(f'{number} x {contador} = {number * contador}')
        contador += 1
    return f'Fim da tabuada do {number}'
    

num_usr = int(input('Digite um número que você queira saber a tabuada: '))
resultado = tabuada(num_usr)
print(resultado)


