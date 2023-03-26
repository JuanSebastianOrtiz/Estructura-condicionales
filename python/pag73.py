

if __name__ == '__main__':
	# Calcular el salario bruto y el salario neto de un trabajador "por horas" conociendo el nombre, numero de horas trabajadas, impuestos a pagar y salario neto.
	# version 1.0 
	# 28/02/2023 
	# programado por:Juan sebastian ortiz
	# definicion de variables
	a = float()
	b = float()
	c = float()
	f = float()
	t = float()
	st = float()
	d = str()
	# inicializacion de las variables 
	a = 0.0
	b = 0.0
	c = 0.0
	e = 0.0
	f = 0.0
	t = 0.0
	d = ""
	st = 0.0
	# captura de datos
	print("Cual es su nombre: ")
	d = input()
	print("Cuanto le pagan por hora: ")
	a = float(input())
	print("Numero horas trabajadas: ")
	b = float(input())
	print("porcentaje del impuesto sin el simbolo %: ")
	c = float(input())
	# procesos aritmeticos
	f = a*b  # formula salario bruto 
	c = c/100 # se divide en 100 para sacar el porcentaje
	t = f*c #formula impuesto
	st = f-t #formula salario total
	# impresion de resultados
	print("trabajador con el nombre: ",d," Su salario bruto es: ",f," Su salario neto es: ",st)

