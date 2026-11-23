nota1 = float(input('digite sua nota: '))
nota2 = float(input('digite sua outra nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
   print('e você está aprovado')
elif media >= 5:
   print('e você está em recuperado')
else:
   print('e você está reprovado')
