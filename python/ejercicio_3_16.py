# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


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
			for i in range(1,n+1):
				# operaciones
				p = p*i
			# impresion de resultado 
			print("el resultado es : ",p)

