soma = 0
for ordem in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(ordem)))
    if numero % 2 == 0:
        soma += numero
print('A soma dos números pares é', soma)