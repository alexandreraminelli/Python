frase = input("Digite uma frase:\n")
frase = frase.lower()

quantidade = frase.count('a')
primeira = frase.find('a')
ultima = frase.rfind('a')

print("Na sua frase, aparece a letra \"A\" {} vezes. Ela aparece pela primeira vez na {}ª posição e na última vez na {}ª posição.".format(quantidade, primeira, ultima))
