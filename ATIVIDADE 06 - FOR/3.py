qtd = 0
n = int(input('digite um numero: '))
for i in range(1, n+1):
    if n % i == 0:
        qtd = qtd + 1
#sei la
if qtd == 2:
    print('é primo')
else:
    print('não é primo')
