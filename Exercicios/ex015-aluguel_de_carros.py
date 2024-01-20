km = float(input('Quantos quilometros o carro andou? '))
dias = float(input('Por quantos dias o carro foi alugado? '))

print('O valor do aluguel do carro é de R${:.2f}'.format(
    km * 0.15 + dias * 60))
