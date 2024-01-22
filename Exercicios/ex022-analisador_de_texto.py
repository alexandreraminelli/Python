nome = input("Digite seu nome: ")
nome = ' '.join(nome.split())

print(nome.upper())
print(nome.lower())

print("Seu nome possui {} letras.".format(len(''.join(nome.split()))))

print("Seu primeiro nome tem {} letras.".format(len(nome.split()[0])))
