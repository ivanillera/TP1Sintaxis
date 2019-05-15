TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta else
def d_else(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "e":
        return 1
    if estado_anterior == 1 and caracter == "l":
        return 2
    if estado_anterior == 2 and caracter == "s":
        return 3
    if estado_anterior == 3 and caracter == "e":
        return 4

    
    return TRAMPA

#automata else
def a_else(cadena):
    Finales = [4]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_else(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("else", RESULTADO_ACEPTADO),
    ("el", RESULTADO_NO_ACEPTADO),
    ("h", RESULTADO_TRAMPA),
    ("1", RESULTADO_TRAMPA),
    ("el se", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_else(cadena)))
    assert a_else(cadena) == resultado