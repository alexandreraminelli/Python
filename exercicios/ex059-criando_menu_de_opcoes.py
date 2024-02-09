from time import sleep

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

acao = ''
while acao != 5:
    acao = int(input('''\nEscolha uma ação para realizar com os números {} e {}: 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    > '''.format(num1, num2)))

    # 1- Somar
    if acao == 1:
        print('SOMANDO...')
        sleep(2)
        soma = num1 + num2
        print('A soma entre {} e {} é igual a {}'.format(num1, num2, soma))

    # 2- Multiplicar
    if acao == 2:
        print('MULTIPLICANDO...')
        sleep(2)
        multiplo = num1 * num2
        print('A multiplicação entre {} e {} é {}'.format(num1, num2, multiplo))

    # 3- Maior
    if acao == 3:
        print('Analisando o MAIOR NÚMERO...')
        sleep(2)
        if num1 > num2:
            print('O primeiro número, {}, é maior.'.format(num1))
        elif num2 > num1:
            print('O segundo número, {}, é o maior.'.format(num2))
        else:
            print('Ambos os números são iguais: {}.'.format(num1))

    # 4- Novos números
    if acao == 4:
        altera = input('Qual número você deseja alterar [n1/n2]? ').lower()
        while not (altera == 'n1' or altera == 'n2'):
            altera = input(
                'Entrada inválida!.\nQual número você deseja alterar [n1/n2]? ').lower()
        if altera == 'n1':
            num1 = int(input('Alterar número {} para: '.format(num1)))
        elif altera == 'n2':
            num2 = int(input('Alterar número {} para: '.format(num2)))

# 5- Sair do programa
print('\n', '='*50)
print('PROGRAMA ENCERRADO!')
