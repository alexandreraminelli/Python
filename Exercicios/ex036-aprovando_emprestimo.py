valorcasa = float(input('Qual o valor do imóvel desejado? R$'))
salario = float(input('Quanto é seu salário? R$'))
anos = int(input('Em quantos ano você pretende pagar o empréstimo? '))

prestacao = valorcasa / (anos * 12)

if prestacao < (salario * 0.3):
    print('SEU EMPRÉSTIMO FOI APROVADO! :)')
    print('O valor da prestação mensal é de R${:.2f}'.format(prestacao))
else:
    print('EMPRÉSTIMO NEGADO!')
    print('O valor da prestação mensal, R${:.2f}, ultrapassa 30% do valor do seu salário!'.format(prestacao))
