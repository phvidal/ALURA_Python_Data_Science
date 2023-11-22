"""
Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome.

As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

"""
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

for nome in nome_completo:
    print(nome)

# def nome_completo(nome, sobrenome):
#     nova_lista = zip(nome, sobrenome)
#     nova_lista = list(nova_lista)
#     return nova_lista

# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]
# resultado = nome_completo(nomes, sobrenomes)
# print(resultado)
# print(type(resultado[0]))