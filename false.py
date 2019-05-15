TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

#delta false
def d_false(estado_anterior, caracter):
	if estado_anterior == 0 and caracter == "f":
		return 1
	if estado_anterior == 1 and caracter == "a":
		return 2
	if estado_anterior == 2 and caracter == "l":
		return 3
	if estado_anterior == 3 and caracter == "s":
		return 4
	if estado_anterior == 4 and caracter == "e":
		return 5

	
	return TRAMPA

#automata false
def a_false(cadena):
	Finales = [5]
	estado_actual = 0

	for caracter in cadena:
		estado_proximo = d_false(estado_actual, caracter)
		if estado_proximo == TRAMPA:
			return RESULTADO_TRAMPA
		estado_actual = estado_proximo
	
	if estado_actual in Finales:
		return RESULTADO_ACEPTADO
	else:
		return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
	("false", RESULTADO_ACEPTADO),
	("fa", RESULTADO_NO_ACEPTADO),
	("'", RESULTADO_TRAMPA),
]

for cadena, resultado in casos:
	print((cadena, a_false(cadena)))
	print( a_false(cadena) == resultado)
