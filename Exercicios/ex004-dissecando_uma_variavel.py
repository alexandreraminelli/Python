variavel = input('Digite algo: ')

print('Essa variável é do tipo {}.'.format(type(variavel)))

print('Pode ser convertida para tipo numérico?:', variavel.isnumeric())

print('É alfabético?:', variavel.isalpha())
print('É alfanumérico?:', variavel.isalnum())
print('Está tudo em maiúscula?:', variavel.isupper())
print('Está tudo em minúscula?:', variavel.islower())
print('É um espaço em branco?', variavel.isspace())
