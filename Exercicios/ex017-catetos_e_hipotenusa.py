from math import sqrt, pow

cat1 = float(input("Qual o comprimento do cateto adjacente em cm? "))
cat2 = float(input("E do cateto oposto?"))

hip = sqrt(pow(cat1,2) + pow(cat2,2))

print("Com base nesses valores, a hipotenusa do triângulo possui {} cm".format(hip))