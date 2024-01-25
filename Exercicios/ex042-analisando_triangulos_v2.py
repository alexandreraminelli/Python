reta1 = float(input('Comprimento da 1ª reta: '))
reta2 = float(input('Comprimento da 2ª reta: '))
reta3 = float(input('Comprimento da 3ª reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    if reta1 == reta2 == reta3:
        print('Essas 3 retas podem formar um triângulo equilátero.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Essas 3 retas podem formar um triângulo isósceles')
    else:
        print('Essas 3 retas podem formar um triângulo escaleno.')
else:
    print('Infelizmente, essas retas não podem formar um triângulo!')