salario = float(input('digite o seu salario: '))
anos = int(input('digite quantos anos voce trabalha na empresa: '))
if anos < 2:
   bonus = 0.0
elif anos <= 5:
   bonus = salario * 0.05
elif salario < 3000:
   bonus = salario * 0.10
else:
   bonus = salario * 0.15
salario_final = salario + bonus
print('salario original' , salario , 'valor do bonus' , bonus , 'salario final' , salario_final)
