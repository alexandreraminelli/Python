import math

angulo = float(input("Digite um ângulo: "))

# Converter angulo em radianos pro math calcular
rad = math.radians(angulo)

sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print("O ângulo de {}° tem: \nSeno = {:.2f} \nCosseno = {:.2f} e \nTangente = {:.2f}".format(angulo, sen, cos, tan))
