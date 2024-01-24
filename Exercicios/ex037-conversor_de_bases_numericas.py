numero = int(input('Digite um número: '))

conversao = int(input('Informe a base de conversão:\n1- Binário\n2- Octal\n3- Hexadecimal\nInsira o dígito correspondente: '))

if conversao == 1:
    print('Convertendo para binário...')
    print(bin(conversao))
elif conversao == 2:
    print('Convertendo para octal...')
    print(oct(conversao))
elif conversao == 3:
    print('Convertendo para hexadecimal...')
    print(oct(conversao))
else:
    print('Você digitou uma base inválida!\nTente novamente!')