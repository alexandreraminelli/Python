numero = int(input('Digite um número: '))

print('CALCULANDO FATORIAL...')

print('{}! = {}'.format(numero, numero), end='')

multiplo = numero - 1
fatorial = numero
while multiplo > 0:
    print(' x', multiplo, end='')
    fatorial = multiplo * fatorial
    multiplo -= 1

print(' =', fatorial)
