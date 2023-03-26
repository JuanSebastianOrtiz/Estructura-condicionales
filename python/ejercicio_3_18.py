 
if __name__ == '__main__':
	# programa que lee 3 numeros enteros y imprime el mayor //
	# desarrollador juan sebastian ortiz ibarra //
	# fecha 19/02/2023//
	# version 1.0//
	# Declaracion de variables 
	a = int()
	b = int()
	c = int()
	# inicializacion de las variables 
	a = 0
	b = 0
	c = 0
	# captura de  datos//
	print("digite el valor del primer numero ")
	a = int(input())
	print("digite el valor del segundo numero ")
	b = int(input())
	print("digite el valor del tercer numero ")
	c = int(input())
	# condicionales y impresion de resultados
	if a>b:
		print("el numero mayor es: ",a)
	else:
		if b>c:
			print("el numero mayor es: ",b)  # este ciclo determina cual es la variable con mayor valor 
		else:
			print("el numero mayor es: ",c)

