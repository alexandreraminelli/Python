num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print("O primeiro valor, {}, é maior que o segundo, {}.".format(num1, num2))
elif num1 < num2:
    print('O segundo valor, {}, é maior que o primeiro, {}.'.format(num2, num1))
else:
    print('Ambos os valores são os mesmos: {}.'.format(num1))