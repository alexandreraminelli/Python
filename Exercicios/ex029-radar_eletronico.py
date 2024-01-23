from time import sleep
velocidade = int(input('Quantos km/hs você estava correndo? '))

print('CALCULANDO...')
sleep(2)

if velocidade > 80:
    multa = float((velocidade - 80) * 7)
    print('Por estar correndo {}km/h, que é {}km/h acima do permitido, você foi multado em R${:.2f}.\nPAGUE A MULTA OU TERÁ SUA LICENÇA CASSADA!'.format(velocidade, (velocidade - 80), multa))
else:
    print('Você está dentro do limite de velocidade permitido.\nTenha um bom dia!')