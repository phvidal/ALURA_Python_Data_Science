"""
Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, 
você precisa criar uma função que receba uma lista de 4 notas e retorne:

    maior nota
    menor nota
    média
    situação (Aprovado(a) ou Reprovado(a))

Para testar o comportamento da função, os dados podem ser exibidos em um texto:

"O(a) estudante obteve uma media de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"
"""

def media_alunos(lista):
    maior_nota = max(lista)
    menor_nota = min(lista)
    media = sum(lista) / len(lista)
    situacao = 'Aprovado' if media > 6 else 'Reprovado'

    return f'O(a) estudante obteve uma media de {media:.2f}, com a sua maior nota de {maior_nota} pontos e a menor nota de {menor_nota} pontos e foi {situacao}'

notas = [10, 8, 6, 7.5, 3, 9.5]
resultado = media_alunos(notas)
print(resultado)