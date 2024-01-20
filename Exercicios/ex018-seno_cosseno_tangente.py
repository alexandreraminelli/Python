import math
#VER RESOLUÇÃO
angulo = float(input("Digite um angulo: "))

#Converter angulo em radianos pro math calcular
rad = math.radians(angulo)

sen = math.sinh(rad)
cos = math.cosh(rad)
tan = math.tanh(rad)

print("O ângulo de {}° tem: \nSeno = {} \nCosseno = {} e \nTangente = {}".format(angulo, sen, cos, tan))