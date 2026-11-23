soma = 0
qtd = 0
for i in range(1, 11):
    n = int(input('digite um numero: '))
    if n > 0:
        soma = soma + n
        qtd = qtd + 1
if qtd > 0:
    media = soma / qtd
    print('media dos positivos:', media)
else:
    print('não foi possível calcular a média')
