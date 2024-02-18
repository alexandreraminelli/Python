numeros = []
quantidade = 0

resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite um número: '))
    numeros.append(numero)  # Adiciona o número na lista
    quantidade += 1

    resposta = str(input('Deseja continuar? [S/N] ')).upper()

numeros.sort()  # Ordenar lista

media = sum(numeros) / len(numeros)
maior = numeros[len(numeros) - 1]
menor = numeros[0]

print('''Você digitou {} números.
      Média: {}
      Maior número: {}
      Menor número: {}'''.format(quantidade, media, maior, menor))
