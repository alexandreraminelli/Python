print('SEQUÊNCIA DE FIBONACCI')
primeiro_termo = int(input('Digite o primeiro termo: '))
segundo_termo = int(input('Digite o segundo termo: '))
quant = int(input('Quantos termos você deseja ver? '))

print('{} → {} → '.format(primeiro_termo, segundo_termo), end='')

contador = 1
while contador <= (quant - 2):
    proximo_termo = primeiro_termo + segundo_termo

    primeiro_termo = segundo_termo
    segundo_termo = proximo_termo

    contador += 1

    print(proximo_termo, end=' → ')

print('...')
