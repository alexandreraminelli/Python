from random import shuffle

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')

ordem = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordem)

print('\nA ordem de apresentação será:')
print('1- {}\n2- {}\n3- {}\n4- {}'.format(*ordem))
