"""
Você foi contratado(a) como cientista de dados de uma associação de skate. 
Para analisar as notas recebidas dos(as) skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. 
Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram.

Retorne a média para apresentar o texto: "Nota da manobra: [media]"

"""

notas = []

for nota in range(0, 5):
    nota = float(input('Digite sua nota: '))
    notas.append(nota)

def media_notas(lista):
    menor_nota = min(notas)
    maior_nota = max(notas)
    print(f'Essa é a menor nota: {menor_nota}')
    print(f'Essa é a maior nota: {maior_nota}')

    notas.remove(min(notas))
    notas.remove(max(notas))
    print(f'Essas são as notas válidas para essa manobra: {notas}')
    return sum(notas) / len(notas)

teste = media_notas(notas)
print(f'Nota da manobra: {teste:.2f}')

# def media(lista):
#   lista.remove(max(lista))
#   lista.remove(min(lista))
#   return sum(lista) / len(lista)

# teste = media(notas)
# print(teste)

