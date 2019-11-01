#calculadora em python

print('############ Python Calculadora ############')

print('Selecione o numero da operação desejada!\n')

print(' 1:Soma\n 2:Subtração\n 3:Multiplicação\n 4:Divisão')

opcao = int (input('Digite sua opção 1/2/3/4:'))

while opcao<1 or opcao>4 :
		opcao = int (input('Digite sua opção novamente 1/2/3/4:'))	

def recebedoUsuario(opcao):

	numero1 = int (input('Digite o primeiro numero:'))
	numero2 = int (input('Digite o segundo numero:'))
	
	if opcao == 1:
		return numero1 + numero2
	elif opcao == 2:
		return numero1 - numero2
	elif opcao == 3:
		return numero1 * numero2
	elif opcao == 4:
		return numero1 / numero2

resultado = recebedoUsuario(opcao)
print(resultado)



