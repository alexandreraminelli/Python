import random
from time import sleep

print('ADIVINHE O NÚMERO!!!')
numero = random.randint(0, 5000)
palpites = 1

resposta = int(input('Em que número eu pensei (entre 0 e 5000)? '))
# efeito de tela de carregamento
print('PROCESSANDO...')
sleep(1)

while numero != resposta:
    if numero > resposta:
        resposta = int(input('Mais... Tente novamente: '))
    else:
        resposta = int(input('Menos... Tente novamente: '))
    palpites += 1
    # efeito de tela de carregamento
    print('PROCESSANDO...')
    sleep(1)

print('\nPARABÉNS!!! Você acertou!\nO número era {}.\nVocê fez {} palpites'.format(
    numero, palpites))
