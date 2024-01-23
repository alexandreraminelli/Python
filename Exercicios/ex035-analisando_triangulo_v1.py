reta1 = float(input('Comprimento da 1ª reta: '))
reta2 = float(input('Comprimento da 2ª reta: '))
reta3 = float(input('Comprimento da 3ª reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Essas 3 retas PODEM formar um triângulo!')
else:
    print('Infelizmente, essas retas NÃO PODEM format um triângulo!')