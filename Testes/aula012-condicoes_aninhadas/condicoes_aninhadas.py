nome = str(input('Qual é seu nome?'))

if nome == 'Alexandre':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Nome legal!')
else:
    print('Seu nome é tão comum :|')

print('Tenha um bom dia {}'.format(nome))