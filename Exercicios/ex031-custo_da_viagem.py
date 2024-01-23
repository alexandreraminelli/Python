print('BEM-VINDO AO SISTEMA DE VIAGENS!')
distancia = float(input('O seu destino está a quantos quilômetros? '))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print('Por seu destino estar a {}km, sua passagem custará R${:.2f}!\nAPROVEITE A VIAGEM!'.format(distancia, preco))