 

if __name__ == '__main__':
	# programa que calcula el factorial de un numero 
	# version 1.0 
	# 3/03/2023
	# programado por:Juan sebastian ortiz
	# definicion de variables
	n = int()
	p = int()
	i = int()
	# lectura de datos
	n = 0
	# captura de datos 
	print("Digite un numero NATURAL(son los enteros positivos)")
	n = int(input())
	# inicializacion de las variables 
	p = 1
	i = 1
	# condicicionales Y procesos aritmeticos
	if n==0:
		print("el factorial de 0 es = 1 ")
	else:
		if n<0:
			print("No se pueden processar numeros negativos")
		else:
			# ciclo y procesos aritmeticos 
			for i in range(1,n+1): # ciclo para con paso en 1 hasta el numero que digite el usuario 
				# operaciones
				p = p*i #formula de factorial 
			# impresion de resultado 
			print("el resultado es : ",p)

