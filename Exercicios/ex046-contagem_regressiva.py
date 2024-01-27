import emoji
from time import sleep

print('Iniciando contagem regressiva...')
sleep(1)

for c in range(10, 0, -1):
    print(c)
    sleep(1)

print(emoji.emojize(":fireworks: "*50))
