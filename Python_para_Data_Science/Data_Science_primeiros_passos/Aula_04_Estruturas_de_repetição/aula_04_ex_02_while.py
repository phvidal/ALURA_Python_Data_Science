"""
Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria "A" ultrapassar ou igualar a colônia de uma bactéria "B", 
com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia "A" inicia com 4 elementos e a colônia "B" com 10 elementos.

"""
bac_a = 4
bac_b = 10

dia = 0

crescimento_a = 0.03
crescimento_b = 0.015

while bac_a <= bac_b:
    bac_a *= 1 + crescimento_a
    bac_b *= 1 + crescimento_b
    dia += 1

print(f'Levou {dia} dias para a primeiro colônia de bactérias "A" ultrapassar a segunda colônia de bactérias "B"')
