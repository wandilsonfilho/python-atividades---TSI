n = int(input('digite um numero: '))
for i in range(1, 21):
    res = n * i
    if res % 2 == 0:
        print(n, 'x', i, '=', res)
