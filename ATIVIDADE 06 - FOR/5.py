pares = 0
impares = 0
for i in range(1, 11):
    n = int(input('digite um numero: '))
    if n % 2 == 0:
        pares = pares + 1
    elif n % 2 == 1:
        impares = impares + 1
#sei la
print('qtd de pares: ', pares)
print('qtd de impares: ', impares)
