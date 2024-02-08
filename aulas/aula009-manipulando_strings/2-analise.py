frase = "Curso em Vídeo Python"
print(frase)

print('Comprimento:', len(frase))

print('Quantas vezes aparece \'o\':', frase.count('o'))
print('Quantas vezes aparece \'o\' entre os caracteres 0 e 13:', frase.count('o', 0, 13))

print('Quantas vezes aparece \'deo\':', frase.find('deo'))
print('Quantas vezes aparece \'Android\':', frase.find('Android'))

print('Existe \'Curso\' dentro da frase?', 'Curso' in frase)
print('Existe \'Android\' dentro da frase?', 'Android' in frase)
