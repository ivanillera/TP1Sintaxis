TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta and
def d_and(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "a":
        return 1
    if estado_anterior == 1 and caracter == "n":
        return 2
    if estado_anterior == 2 and caracter == "d":
        return 3    
    return TRAMPA

#automata and
def a_and(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_and(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("and", RESULTADO_ACEPTADO),
    ("an", RESULTADO_NO_ACEPTADO),
    ("b", RESULTADO_TRAMPA),
    ("5", RESULTADO_TRAMPA),
    ("an d", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_and(cadena)))
    assert a_and(cadena) == resultado
