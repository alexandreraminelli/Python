from random import choice
print('JOKENPÔ')

jogador = input("Pedra, papel ou tesoura? ")
jogador = jogador.lower()

computador = choice(['pedra', 'papel', 'tesoura'])

print('{} X {}'.format(jogador, computador))

if jogador == 'pedra':
    if computador == 'pedra':
        print('EMPATE')
    elif computador == 'papel':
        print('DERROTA')
    else:
        print('VITÓRIA')
elif jogador == 'papel':
    if computador == 'pedra':
        print('VITÓRIA')
    elif computador == 'papel':
        print('EMPATE')
    else:
        print('DERROTA')
elif jogador == 'tesoura':
    if computador == 'pedra':
        print('DERROTA')
    elif computador == 'papel':
        print('VITÓRIA')
    else:
        print('EMPATE')
else:
    print('Você não digitou um valor válido!')
