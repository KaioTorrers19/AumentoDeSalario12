salario = float(input('digite um salario'))
aumento = salario+(salario *5 /100)

print('o salario de R${:.2f} com aumento de 5% do salario será R${:.2f}'.format(salario, aumento))