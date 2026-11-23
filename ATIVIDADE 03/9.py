compra = float(input('digite o valor de sua compra: '))
if compra < 100:
   print('valor original' , compra , 'valor do desconto 0' , 'valor a ser pago' , compra)
elif compra <= 499.99:
   desconto = compra / 0.10
   print('valor original' , compra , 'valor do desconto 10%' , 'valor a ser pago' ,desconto)
else:
   desconto2 = compra / 0.15
   print('valor original', compra, 'valor do desconto 15%', 'valor a ser pago', desconto2)
