 


if __name__ == '__main__':
	# programa que  que suma los numeros naturales pares ,hasta el numero 100
	# version 1.0 
	# 27/02/2023 
	# programado por:Juan sebastian ortiz
	# definicion de variables
	s = int()
	n = int()
	p = int()
	# inicializacion de las variables
	s = 0
	p = 0
	n = 100
	# bucle operaciones aritmeticas 
	for s in range(1,n+1): # ciclo para hasta el 100 de uno en 1 
		# condicional
		if s%2==0: #en este caso si el residuo de la division da = 2 se procede por la operacion
			p = p+s #formula de suma ,suma los numeros que cumplieran la condicion de modular 2
	# impresion de resultado
	print("el resultado de la suma de los numeros pares hasta el numero 100 es: ",p)

