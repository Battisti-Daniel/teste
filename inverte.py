palavra = str(input("Digite a palavra a ser invertida: "))

reverse = ''

for i in range(1, len(palavra) + 1):
    reverse += palavra[-i]

print(reverse)
