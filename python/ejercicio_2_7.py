# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# programa que calcula la media de una sucesion de numeros positivos y calcula la media cuando se digita en la terminal de la entrada un 0
	# version 1.0 
	# 3/03/2022
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
	while True:# no hay 'repetir' en python
		dato = int(input())
		if dato!=0:
			# procesos aritmeticos
			c = c+1
			s = s+dato
		# numero que finaliza la secuencia de numeros positivos
		if dato==0: break
	# finalizacion de numeros positivos
	if (c>0):
		media = s/c
		# impresion de resultado
		print("La media es: ",(media))

