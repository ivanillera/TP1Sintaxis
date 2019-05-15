TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta return
def d_return(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "r":
        return 1
    if estado_anterior == 1 and caracter == "e":
        return 2
    if estado_anterior == 2 and caracter == "t":
        return 3
    if estado_anterior == 3 and caracter == "u":
        return 4
    if estado_anterior == 4 and caracter == "r":
        return 5 
    if estado_anterior == 5 and caracter == "n":
        return 6

    
    return TRAMPA

#automata return
def a_return(cadena):
    Finales = [6]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_return(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("return", RESULTADO_ACEPTADO),
    ("ret", RESULTADO_NO_ACEPTADO),
    ("1", RESULTADO_TRAMPA),
    ("return:", RESULTADO_TRAMPA),
    ("retur7n", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_return(cadena)))
    assert a_return(cadena) == resultado