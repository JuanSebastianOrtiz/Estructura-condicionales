# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


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
	# lectura de los datos//
	print("digite el valor del primer numero ")
	a = int(input())
	print("digite el valor del segundo numero ")
	b = int(input())
	print("digite el valor del tercer numero ")
	c = int(input())
	# condicionales///impresion de resultados
	if a>b:
		print("el numero mayor es: ",a)
	else:
		if b>c:
			print("el numero mayor es: ",b)
		else:
			print("el numero mayor es: ",c)

