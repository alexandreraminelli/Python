lista = []

for ordem in range(1, 6):
    peso = float(input('Qual é o peso da {}ª pessoa (em kg): '.format(ordem)))
    lista.append(peso)
    
lista.sort() #Ordena os valores da lista do maior pro maior
print(lista)

print('O maior peso é {}kg e o menor peso é {}kg.'.format(lista[4], lista[0]))