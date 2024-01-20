import random

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')

print('O aluno que foi escolhido para ajudar foi {}.'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))