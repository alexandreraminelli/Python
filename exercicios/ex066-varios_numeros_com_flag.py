contador = soma = 0
while True:
    numero = int(input('Digite um valor: '))
    if numero != 999:
        contador += 1
        soma += numero
    else:
        break
print(f'A soma dos {contador} valores é {soma}!')
