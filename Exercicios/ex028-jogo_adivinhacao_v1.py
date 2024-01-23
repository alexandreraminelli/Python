import random
from time import sleep

print('ADIVINHE O NÚMERO!!!')
numero = random.randint(0,5)

resposta = int(input('Em que número eu pensei (entre 0 e 5)?\n'))
# efeito de tela de carregamento
print('PROCESSANDO...')
sleep(2)

if numero == resposta:
    print('PARABÉNS!!! Você acertou!\nO número era {}'.format(numero))
else:
    print('QUE PENA! A resposta era {}!'.format(numero))