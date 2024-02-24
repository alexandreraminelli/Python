sacar = int(input('Valor para sacar: R$'))

quant_50 = quant_20 = quant_10 = quant_1 = 0

# Notas de 50
while sacar >= 50:
    sacar -= 50
    quant_50 += 1
# Notas de 20
while sacar >= 20:
    sacar -= 20
    quant_20 += 1
# Notas de 10
while sacar >= 10:
    sacar -= 10
    quant_10 += 1
while sacar >= 1:
    sacar -= 1
    quant_1 += 1

if sacar == 0:
    print('Quantidade de notas de R$50:', quant_50)
    print('Quantidade de notas de R$20:', quant_20)
    print('Quantidade de notas de R$10:', quant_10)
    print('Quantidade de notas de R$1:', quant_1)
