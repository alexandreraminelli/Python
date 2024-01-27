from datetime import date
ano_atual = date.today().year

maiores = []
menores = []

for ordem in range(1, 8):
    nome = input('Nome da {}ª pessoa: '.format(ordem))
    idade = ano_atual - int(input("Ano de nascimento da {}ª pessoa: ".format(ordem)))
    if idade >= 18:
        maiores.append(nome)
    else:
        menores.append(nome)

print('Os maiores de idade são: {}.'.format(maiores))
print('Os menores de idade são: {}.'.format(menores))