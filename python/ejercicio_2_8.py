# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# progrma que  que suma los numeros naturales pares ,hasta el numero 100
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
	for s in range(1,n+1):
		# condicional
		if s%2==0:
			p = p+s
	# impresion de resultado
	print("el resultado de la suma de los numeros pares hasta el numero 100 es: ",p)

