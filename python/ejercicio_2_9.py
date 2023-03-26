 

if __name__ == '__main__':
	# programa que calcula el salario de un empleado 
	# version 1.0 
	# 28/02/2022
	# programado por:Juan sebastian ortiz
	# definicion de variables
	a = float()
	b = float()
	f = float()
	t = float()
	st = float()
	d = str()
	# inicializacion de la variables
	a = 0.0
	b = 0.0
	f = 0.0
	t = 0.0
	st = 0.0
	d = ""
	# captura de datos
	print("Cual es su nombre: ")
	d = input()
	print("Cuanto le pagan por hora: ")
	a = float(input())
	print("Numero horas trabajadas: ")
	b = float(input())
	# procesos 
	f = a*b # formula pago en caso de que no sea mayor a 40
	if b>40:
		f = a*40 #formula pago 
		t = ((b-40)*a)*1.5 #formula pago horas adicionales
	st = f+t    #formula del salario neto 
	# impresion de resultados
	print("trabajador con el nombre: ",d," Su salario neto es: ",st)

