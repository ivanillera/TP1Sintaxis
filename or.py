TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta or
def d_or(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "o":
        return 1
    if estado_anterior == 1 and caracter == "r":
        return 2
    return TRAMPA

#automata or
def a_or(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_or(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("or", RESULTADO_ACEPTADO),
    ("o", RESULTADO_NO_ACEPTADO),
    ("t", RESULTADO_TRAMPA),
    ("2", RESULTADO_TRAMPA),
    ("o r", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_or(cadena)))
    assert a_or(cadena) == resultado
