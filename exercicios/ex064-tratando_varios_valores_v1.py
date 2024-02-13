print('Condição de parada: 999 (este número não é considerado!)')

numero = int(input('Digite um número: '))
soma = 0
contador = 0

while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número: '))

print('Você digitou {} números e a soma deles é {}.'.format(contador, soma))
