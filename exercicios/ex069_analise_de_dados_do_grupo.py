print('CADASTRO DE PESSOAS')

mais_18 = homens = mulheres_menos_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while not (sexo == 'M' or sexo == 'F'):
        sexo = str(input('Entrada inválida.\nSexo [M/F]: ')).strip().upper()

    if idade > 18:
        mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break

print('Total de pessoas com mais de 18 anos:', mais_18)
print('Quantidade de homens cadastrados:', homens)
print('Quantidade de mulheres com menos de 20 anos:', mulheres_menos_20)
