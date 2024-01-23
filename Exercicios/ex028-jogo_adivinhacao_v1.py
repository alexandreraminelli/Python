import random

print('ADIVINHE O NÚMERO!!!')
numero = random.randint(0,5)

resposta = int(input('Em que número eu pensei (entre 0 e 5)?\n'))
if numero == resposta:
    print('PARABÉNS!!! Você acertou!\nO número era {}'.format(numero))
else:
    print('QUE PENA! A resposta era {}!'.format(numero))