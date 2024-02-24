preço = total = mais_de_mil = 0
menor_preço = ''

while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    # Total da compra
    total += preço
    # Mais de mil
    if preço > 1000:
        mais_de_mil += 1
    # Produto e preço mais baratos
    if menor_preço == '':
        mais_barato = produto
        menor_preço = preço
    elif preço < menor_preço:
        mais_barato = produto
        menor_preço = preço
    # Continuar?
    continuar = input('Continuar compra? [S/N]').strip().upper()[0]
    if continuar != 'S':
        break

print('\n{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra é R${total:.2f}')
print(f'Temos {mais_de_mil} produtos com o preço maior que R$1.000,00')
print(f'O produto mais barato foi {mais_barato} que custa R${menor_preço:.2f}')
