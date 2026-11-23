soma = 0
for i in range(1, 201):
    if i % 5 == 0:
        soma = soma + 1
        print(i)
print(' qtd de divisiveis: ', soma)
