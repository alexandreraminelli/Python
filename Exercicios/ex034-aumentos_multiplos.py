salarioatual = float(input('Qual é seu salário atual? R$'))

if salarioatual > 1250:
    salarionovo = salarioatual * 1.1
else:
    salarionovo = salarioatual * 1.15

print('Com o novo reajuste, seu salário agora é de R${:.2f}.'.format(salarionovo))