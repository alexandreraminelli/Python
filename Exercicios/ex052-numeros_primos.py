numero = int(input("Digite um número inteiro: "))

divisores = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[34m', end='')
        divisores += 1
    else:
        print('\033[m', end='')
    print(c, end=' ')
print('\n\033[35m')

print('O número {} tem {} divisores'.format(numero, divisores), end='')
if divisores == 2:
    print(': 1 e ele mesmo. \nEntão, ele É PRIMO!')
else:
    print('. \nPortanto, ele NÃO É PRIMO!')

print('\033[m')
