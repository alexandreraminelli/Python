largura = float(input('Qual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))

metros = largura * altura

print('A parede possui {:.2f} m², portanto serão necessários {:.0f} litros de tinta.'.format(
    metros, metros//2))
