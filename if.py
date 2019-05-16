TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta if
def d_if(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "i":
        return 1
    if estado_anterior == 1 and caracter == "f":
        return 2
    return TRAMPA

#automata if
def a_if(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_if(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("if", RESULTADO_ACEPTADO),
    ("i", RESULTADO_NO_ACEPTADO),
    ("f", RESULTADO_TRAMPA),
    ("if  ", RESULTADO_TRAMPA),
    ("1if", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_if(cadena)))
    assert a_if(cadena) == resultado
