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

# mostrar mais termos?
resposta = int(input('Gostaria de ver mais quantos termos? '))
while resposta != 0:
    # Calcular o último termo a ser mostrado
    ultimo_termo = termo + (resposta) * razao
    # Mostrar os termos da PA usando a razão como passo
    for termo_novo in range(termo, ultimo_termo, razao):
        print(termo_novo, end=' → ')
        termo = ultimo_termo + razao
    resposta = int(input('Gostaria de ver mais quantos termos? '))


print('Programa encerrado!')
