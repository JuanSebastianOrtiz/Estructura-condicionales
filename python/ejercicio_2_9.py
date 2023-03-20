# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


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
	f = a*b
	if b>40:
		f = a*40
		t = ((b-40)*a)*1.5
	st = f+t
	# impresion de resultados
	print("trabajador con el nombre: ",d," Su salario neto es: ",st)

