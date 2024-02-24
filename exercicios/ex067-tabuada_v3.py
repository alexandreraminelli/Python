print('TABUADA\nDigite valor negativo para encerrar o programa!')

while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero >= 0:
        for multiplo in range(1, 11):
            print(f'{numero} x {multiplo} = {numero * multiplo}')
    else:
        break
print('-'*30)
print('PROGRAMA TABUADA ENCERRADO')