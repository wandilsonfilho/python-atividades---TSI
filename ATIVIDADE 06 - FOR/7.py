menor = int(input('digite um numero: '))
for i in range(1, 8):
    n = int(input('digite um numero: '))
    if n < menor:
        menor = n
print('o menor numero é:', menor)
