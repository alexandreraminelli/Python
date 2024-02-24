from random import randint

player_vitorias = 0
print('PAR OU ÍMPAR\n')
while True:
    player_num = int(input('Diga um valor: '))
    player_pi = str(input('Par ou Ímpar [P/I]')).upper()
    
    computer_num = randint(1,10)

    soma = player_num + computer_num
    print(f'Você jogou {player_num} e eu {computer_num}. A soma é {soma}')
    
    if soma % 2 == 0:
        print('DEU PAR')
        par_impar = 'P'
    else:
        print('DEU ÍMPAR')
        par_impar = 'I'

    if player_pi == par_impar:
        print('\nVocê VENCEU!')
        player_vitorias += 1
    else:
        print('\nVocê PERDEU!')
        break

print('\nGAME OVER')
print(f'Você venceu {player_vitorias} vezes.')
