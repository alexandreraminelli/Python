sexo = ''
while not (sexo == 'M' or sexo == 'F'):
    sexo = str(input('Digite seu sexo [M/F]: ').upper())
    if not (sexo == 'M' or sexo == 'F'):
        print('Entrada inválida. Digite apenas M ou F!')
print('Seu sexo inserido é {}.'.format(sexo))
