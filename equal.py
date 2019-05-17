TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta equal
def d_equal(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "=":
        return 1
    if estado_anterior == 1 and caracter == "=":
        return 2   
    return TRAMPA

#automata equal
def a_equal(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_equal(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("==", RESULTADO_ACEPTADO),
    ("=", RESULTADO_NO_ACEPTADO),
    ("-", RESULTADO_TRAMPA),
    ("/=", RESULTADO_TRAMPA),
    ("= =", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_equal(cadena)))
    assert a_equal(cadena) == resultado
