n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 + n2
mult = n1 * n2
divi = n1 / n2
divint = n1 // n2
expo = n1 ** n2

print('A soma é {}, \n o produto é {}, \n divisão é {:.3}'.format(
    soma, mult, divi), end=' >>> ')

print('A divisão inteira é {} /n e a potência é {}'.format(divint, expo))
