from math import floor, trunc

# com floor (minha solução)

num1 = float(input("Digite um número: "))

print("A parte inteira de {} é o valor {}".format(num1, floor(num1)))

# com trunc

num2 = float(input("Digite outro número: "))
print("A parte inteira de {} é o valor {}".format(num2, trunc(num2)))

# convertendo para int

num3 = float(input("Digite mais um número: "))
print('A parte inteira de {} é o valor {}'.format(num3, int(num3)))