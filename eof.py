TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta eof
def d_eof(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "e":
        return 1
    if estado_anterior == 1 and caracter == "o":
        return 2
    if estado_anterior == 2 and caracter == "f":
        return 3

    
    return TRAMPA

#automata eof
def a_eof(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_eof(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("eof", RESULTADO_ACEPTADO),
    ("eo", RESULTADO_NO_ACEPTADO),
    ("f", RESULTADO_TRAMPA),
    ("eof ", RESULTADO_TRAMPA),
    ("123", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_eof(cadena)))
    assert a_eof(cadena) == resultado