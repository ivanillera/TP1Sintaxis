TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

#delta punto
def d_punto(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == ".":
		return 1

	
	return TRAMPA

#automata punto
def a_punto(cadena):
	Finales = [1]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_punto(estado_actual, caracter)
		if estado_proximo == TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
	(".", RESULTADO_ACEPTADO),
	("", RESULTADO_NO_ACEPTADO),
	("'", RESULTADO_TRAMPA),
]

for cadena, resultado in casos:
	print((cadena, a_punto(cadena)))
	print( a_punto(cadena) == resultado)
