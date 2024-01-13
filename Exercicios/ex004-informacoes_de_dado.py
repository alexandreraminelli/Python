variavel = input('Digite algo: ')

print('Essa variavel é do tipo {}.'.format(type(variavel)))

print('Pode ser convertida para tipo numério?:', variavel.isnumeric())

print('É alfabético?:', variavel.isalpha())
print('É alfanumérico?:', variavel.isalnum())
print('Está tudo em maiuscula?:', variavel.isupper())
print('Está tudo em minuscula?:', variavel.islower())
print('É um espaço em branco?', variavel.isspace())
