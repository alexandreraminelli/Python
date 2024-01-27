primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

print('Os 10 primeiros termos dessa PA são: ')
for termo in range(primeiro_termo, primeiro_termo + 10 * razao, razao):
    print(termo)
