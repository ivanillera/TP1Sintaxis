TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta while
def d_while(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "w":
        return 1
    if estado_anterior == 1 and caracter == "h":
        return 2
    if estado_anterior == 2 and caracter == "i":
        return 3
    if estado_anterior == 3 and caracter == "l":
        return 4
    if estado_anterior == 4 and caracter == "e":
        return 5

    
    return TRAMPA

#automata while
def a_while(cadena):
    Finales = [5]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_while(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("while", RESULTADO_ACEPTADO),
    ("w", RESULTADO_NO_ACEPTADO),
    ("wh1le", RESULTADO_TRAMPA),
    (" while", RESULTADO_TRAMPA),
    ("While", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_while(cadena)))
    assert a_while(cadena) == resultado