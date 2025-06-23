nome = 'José Roberto'
altura = 1.73
peso = 91
imc = peso / (altura * altura)


#f-strings
linha_1 = f'{nome} tem {altura} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print (linha_1)
print (linha_2)
print (linha_3)