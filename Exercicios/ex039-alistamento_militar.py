from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Em que ano você nasceu? '))

idade = ano_atual - ano_nascimento

if idade < 18:
    print('Você ainda vai se alistar no exército!')
elif idade == 18:
    print('Já é hora de você se alistar!')
else:
    print('Já passou o tempo do seu alistamento!')
