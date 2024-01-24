from datetime import date
ano_atual = date.today().year

print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
ano_nascimento = int(input('Em que ano você nasceu?'))

idade = ano_atual - ano_nascimento
if idade < 9:
    categoria = 'MIRIM'
elif idade < 14:
    categoria = 'INFANTIL'
elif idade < 19:
    categoria = 'JUNIOR'
elif idade < 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

print('Como você tem (ou completa nesse ano) {} anos de idade, você está na categoria {}!'.format(idade, categoria))
