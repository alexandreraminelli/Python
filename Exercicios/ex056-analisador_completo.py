soma_idade = 0

maior_idade_homem = 0
nome_mais_velho = ''

mulheres_jovens = 0

for pessoa in range(1, 5):
    print('{}ª pessoa'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).strip()
    # Soma das idades
    soma_idade += idade

    # Maior idade dos homens
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome

    # Mulher com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        mulheres_jovens += 1

# MÉDIA DE IDADE
media_idade = soma_idade / 4
print('\nA média da idade do grupo é de {} anos'.format(media_idade))

# Homem mais velho?
print('\nO homem mais velho do grupo é o {} com {} anos.'.format(
    nome_mais_velho, maior_idade_homem))

# Quantas mulheres com menos de 20?
print('\nHá {} mulheres com menos de 20 anos.\n'.format(mulheres_jovens))
