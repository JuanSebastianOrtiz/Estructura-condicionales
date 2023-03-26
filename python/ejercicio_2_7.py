 


if __name__ == '__main__':
	# programa que calcula la media de una sucesion de numeros positivos y calcula la media cuando se digita en la terminal de la entrada un 0
	# version 1.0 
	# 3/03/2023
	# programado por:Juan sebastian ortiz
	# definicion de variables
	dato = int()
	c = int()
	media = float()
	s = float()
	# inicializacion de las variables
	c = 0
	s = 0.0
	media = 0.0
	dato = 0
	# lectura de datos
	print("digite numeros para calcular su media;  para finalizar se introduce 0")
	# condicionales
	while True: # ciclo while mientas
		dato = int(input())
		if dato!=0:
			# procesos aritmeticos
			c = c+1 #cuentas los numeros digitados 
			s = s+dato # variable donde se suman sucesivamente los datos 
		# numero que finaliza la secuencia de numeros positivos
		if dato==0: break #cuando el usuario digite el 0 acaba el ciclo while y se realiza el proceso con los numeros dados
	# finalizacion de numeros positivos
	if (c>0): 
		media = s/c  #formula media 
		# impresion de resultado
		print("La media es: ",(media))

