primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(
    input('Qual é a razão da PA (valores negativos para PA decrescente): '))

termo = primeiro_termo

# razao positiva
if razao > 0:
    while termo < (primeiro_termo + 10 * razao):
        print(termo, end=' → ')
        termo += razao
# razao negativa
else:
    while termo > (primeiro_termo + 10 * razao):
        print(termo, end=' → ')
        termo += razao
print('...')
