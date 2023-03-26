Algoritmo  pag_73
	// Calcular el salario bruto y el salario neto de un trabajador "por horas" conociendo el nombre, número de horas trabajadas, impuestos a pagar y salario neto.
	//version 1.0 
	//28/02/2023 
	// programado por:Juan sebastian ortiz
	//definicion de variables
	definir a , b ,c  ,f,t,st como real  
	definir d como caracter
	//inicializacion de las variables 
	a= 0.0
	b =0.0
	c = 0.0
	e =0.0
	f =0.0
	t =0.0 
	d = "" 
	st= 0.0
	//captura de datos
	escribir  "Cual es su nombre: "
	leer d 
	escribir  "Cuanto le pagan por hora: "
	leer a
	escribir "Numero horas trabajadas: "
	leer b
	escribir  "porcentaje del impuesto sin el simbolo %: "
	leer c
	//procesos aritmeticos
	f= a * b //formula salario bruto
	c = c /100 // se divide entre 100 para encontrar el porcentaje
	t = f * c // formula del impuesto
	st = f - t // formula del salario total
	//impresion de resultados
	escribir "trabajador con el nombre: " d " Su salario bruto es: " f " Su salario neto es: " st
	
	
	
FinAlgoritmo