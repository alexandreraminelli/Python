# Jogo da adivinhação - v2.1

# Importações
from random import randint
from time import sleep

# Funções


def espera(mensagem, tempo):
    print(mensagem)
    sleep(tempo)


# Título
print(f'{"Adivinhe o número":=^50}')

# Selecionar intervalo:
while True:
    print('Selecione o intervalo:')
    try:
        minimo = int(input('Mínimo: '))
        maximo = int(input('Máximo: '))
    except ValueError:
        print('Entrada inválida! Digite apenas números!')
    else:
        if minimo > maximo:
            minimo, maximo = maximo, minimo
        break

# Gerar número
resposta = randint(minimo, maximo)

# Adivinhação
tentativa = int(
    input(f'Em que número eu pensei? (entre {minimo} e {maximo}).\n> '))
palpites = 1
espera('PROCESSANDO...', 2)

while resposta != tentativa:
    if resposta > tentativa:
        tentativa = int(
            input(f'Errado! O número é maior que {tentativa}.\n> '))
    else:
        tentativa = int(
            input(f'Errado! O número é menor que {tentativa}.\n> '))
    palpites += 1
    espera('PROCESSANDO...', 2)

print(f'\nPARABÉNS!!! Você acertou!\nO número era {resposta}.\nVocê fez {palpites} palpites.')
