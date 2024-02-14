sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
while not (sexo == 'M' or sexo == 'F'):
    sexo = input('Entrada inválida. Informe seu sexo [M/F]: ').strip().upper()[0]
print('Seu sexo inserido é {}.'.format(sexo))
