from math import sqrt, pow, hypot

# Minha solução (importando sqrt e pow)

cat1 = float(input("Qual o comprimento do cateto adjacente em cm? "))
cat2 = float(input("E do cateto oposto?"))

hip = sqrt(pow(cat1, 2) + pow(cat2, 2))

print("Com base nesses valores, a hipotenusa do triângulo possui {} cm".format(hip))

# Solução com hypot
print("\nVamos calcular novamente\n")

cateto1 = float(input("Cateto adjacente (cm): "))
cateto2 = float(input("Cateto oposto (cm): "))

print("A hipotenusa é {:.2f}".format(hypot(cateto1, cateto2)))
