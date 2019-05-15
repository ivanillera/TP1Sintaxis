TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta igual
def d_igual(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "=":
        return 1

    
    return TRAMPA

#automata igual
def a_igual(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_igual(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("=", RESULTADO_ACEPTADO),
    ("", RESULTADO_NO_ACEPTADO),
    ("==", RESULTADO_TRAMPA),
    (">", RESULTADO_TRAMPA),
    ("a=", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_igual(cadena)))
    assert a_igual(cadena) == resultado