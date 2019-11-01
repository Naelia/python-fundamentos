#Condicionais_em_Python

n = int (input("digite um numero!"))

if n  > 0:
	print("n é maior que 0")
elif n < 0:
	print("n é menor que 0")
else:
	print("O Numero é maior que 1")

#IFs aninhados, nada mais é que um if dentro de um if
nome = input("digite um nome!")
idade = int (input("digite um ano!"))
if nome == "Maria":
	if idade > 18:
		print('ok %s voce pode dirigir, sua idade é %r' %(nome,idade))
	else:
		print('voce nao pode dirigir')
else:
	print('nome invalido')

