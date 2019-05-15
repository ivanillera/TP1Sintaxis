TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta for
def d_for(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "f":
        return 1
    if estado_anterior == 1 and caracter == "o":
        return 2
    if estado_anterior == 2 and caracter == "r":
        return 3

    
    return TRAMPA

#automata for
def a_for(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_for(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("for", RESULTADO_ACEPTADO),
    ("f", RESULTADO_NO_ACEPTADO),
    ("o", RESULTADO_TRAMPA),
    ("1", RESULTADO_TRAMPA),
    ("for:", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_for(cadena)))
    assert a_for(cadena) == resultado