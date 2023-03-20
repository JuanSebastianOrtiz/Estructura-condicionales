# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# programa que segun los minutos de la llamada varia su precio y los pasos
	# version 1.0 
	# 27/02/2023
	# programado por:Juan sebastian ortiz
	# definicion de variables
	l = float()
	p = float()
	c = float()
	pc = float()
	# inicializacion variables
	p = 0.0
	c = 0.0
	l = 0.0
	pc = 0.0
	# captura de datos 
	print("cuantos minutos lleva en la llamada")
	l = float(input())
	# condicionales y procesos aritmeticos
	if l<3:
		print("la llamada tiene un coste de : 10 centimos  (cinco pasos)")
	else:
		# impresion de resultados
		if l>=3:
			p = (l-3)
			c = 10+(p*5)
			pc = p+5
			print("minutos adicionales : ",p," (precio): ",c," pasos del contador: ",pc)

