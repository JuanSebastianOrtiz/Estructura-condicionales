Algoritmo Ejercicio_2_9
	// programa que calcula el salario de un empleado 
	//version 1.0 
	//28/02/2023
	// programado por:Juan sebastian ortiz
	//declaracion de las variables
	definir a , b  ,f,t,st como real  
	definir d como caracter 
	//inicializacion de la variables
	a =0.0
	b=0.0
	f=0.0
	t=0.0
	st=0.0
	d = ""
	//captura de datos
	escribir  "Cual es su nombre: "
	leer d 
	escribir  "Cuanto le pagan por hora: "
	leer a
	escribir "Numero horas trabajadas: "
	leer b
	//procesos 
	f= a * b   // formula pago en caso de que no sea mayor a 40
	si b > 40 entonces 
		f= a * 40  // formula pago 
		t = ((b-40)*a)*1.5   //formula pago horas adicionales 
	FinSi
	st = f +t   //formula del salario neto 
	
	//impresion de resultados
	escribir "trabajador con el nombre: " d  " Su salario neto es: " st
	
	
FinAlgoritmo
