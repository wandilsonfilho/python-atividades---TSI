soma = 0
for i in range(1, 101):
    if i % 3 == 0:
        soma = soma + 1
        print(i)
print(' qtd de multiplo por 3: ', soma)
