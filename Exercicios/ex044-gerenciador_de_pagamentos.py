preco = float(input('Qual é o preço do produto? R$'))
metodo = input("""\nMÉTODOS DE PAGAMENTO DISPONIVÉIS:
a- À vista: Dinheiro/cheque
b- À vista: cartão
c- Em até 2x no cartão
d- 3x ou mais no cartão
Qual método de pagamento você prefere? """)

if metodo == 'a': # vista - dinheiro/cheque
    # 10% de desconto
    preco_novo = preco * 0.9
elif metodo == 'b': # vista - cartao
    # 5% de desconto
    preco_novo = preco * 0.95
elif metodo == 'c': # 2x cartão
    # normal
    preco_novo = preco
elif metodo == 'd': #3x ou + no cartão
    # 20% de juros
    preco_novo = preco * 1.2

print('De acordo com o método de pagamento, o valor do pagamento total é de R${:.2f}'.format(preco_novo))
