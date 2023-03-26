 

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
		 
		if l>=3:
			p = (l-3) #formula de minutos empleados en la llamada 
			c = 10+(p*5) #formulas de precio de la llamada 
			pc = p+5 #formula de pasos del contador
			#impresion de resultados
			print("minutos adicionales : ",p," (precio): ",c," pasos del contador: ",pc)

