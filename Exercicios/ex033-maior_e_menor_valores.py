from time import sleep

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))

print('\nAnalisando os números...\n')
sleep(1.5)

# Maior
if num1 > num2 and num1 > num3:
    print('O número {} é o maior.'.format(num1))
if num2 > num1 and num2 > num3:
    print('O número {} é o maior.'.format(num2))
if num3 > num1 and num3 > num2:
    print('O número {} é o maior.'.format(num3))

#Menor
if num1 < num2 and num1 < num3:
    print('O número {} é o menor.'.format(num1))
if num2 < num1 and num2 < num3:
    print('O número {} é o menor.'.format(num2))
if num3 < num1 and num3 < num2:
    print('O número {} é o menor'.format(num3))