TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

#delta true
def d_true(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "t":
		return 1
	if estado_anterior == 1 and caracter == "r":
		return 2
	if estado_anterior == 2 and caracter == "u":
		return 3
	if estado_anterior == 3 and caracter == "e":
		return 4
	
	
	return TRAMPA

#automata true
def a_true(cadena):
	Finales = [4]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_true(estado_actual, caracter)
		if estado_proximo == TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
	("true", RESULTADO_ACEPTADO),
	("tru", RESULTADO_NO_ACEPTADO),
	("trru", RESULTADO_TRAMPA),
]

for cadena, resultado in casos:
	print((cadena, a_true(cadena)))
	print( a_true(cadena) == resultado)
