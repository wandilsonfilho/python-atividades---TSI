pares = 0
for i in range(1, 51):
    if i % 2 == 0:
        pares = pares + 1
        print(i)
print(' qtd de pares: ', pares)

impares = 1
for i in range(1, 51):
    if i % 2 == 1:
        impares = impares + 1
        print(i)
print(' qtd de impares: ', impares)
