
print('\033[31;44mOlá\033[4m, Mundo!\033[m')

print('\033[7;31;44mTexto\033[m')

print('\033[7mTexto\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Guanabara'

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[1;38;48m', nome, '\033[m'))


cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
