import random
from time import sleep

print('ADIVINHE O NÚMERO!!!')
numero = random.randint(0, 15)
palpites = 0

resposta = int(input('Em que número eu pensei (entre 0 e 15)? '))
# efeito de tela de carregamento
print('PROCESSANDO...')
sleep(1)

while numero != resposta:
    resposta = int(input('Incorreto! Tente novamente: '))
    palpites += 1
    # efeito de tela de carregamento
    print('PROCESSANDO...')
    sleep(1)

print('PARABÉNS!!! Você acertou!\nO número era {}.\nVocê fez {} palpites'.format(
    numero, palpites))
