nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2
print('Sua média é {}.'.format(media))
if media < 5:
    print('REPROVADO')
elif 5 <= media < 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
