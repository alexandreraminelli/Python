from datetime import date
from time import sleep

ano = int(input('Digite um ano: '))

if ano == 0:
    ano = date.today().year

print('Analisando o ano {}...'.format(ano))
sleep(2)

if ano % 4 == 0:
    if ano % 100 != 0:
        print('O ano é BISSEXTO!')
    else:
        if ano % 400 == 0:
            print('O ano é BISSEXTO!')
else:
    print('O ano NÃO é bissexto!')