numero = int(input("Digite um número natural entre 0 e 9999: "))

print("Unidade:", numero // 1 % 10)
print("Dezena:", numero // 10 % 10)
print("Centena:", numero // 100 % 10)
print("Milhar:", numero // 1000 % 10)
