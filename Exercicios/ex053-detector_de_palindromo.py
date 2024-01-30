frase = str(input('Digite uma frase (sem acentos): ')).strip().upper()

# Retirar espaços da frase
palavras = frase.split()
frase_junto = ''.join(palavras)

frase_inversa = frase_junto[::-1]

print('A frase {} invertida é {}.'.format(frase_junto, frase_inversa))
if frase_junto == frase_inversa:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
