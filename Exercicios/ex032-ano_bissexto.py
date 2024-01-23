ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    if ano % 100 != 0:
        print('O ano é BISSEXTO!')
    else:
        if ano % 400 == 0:
            print('O ano é BISSEXTO!')
else:
    print('O ano NÃO é bissexto!')