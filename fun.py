TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta fun
def d_fun(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "f":
        return 1
    if estado_anterior == 1 and caracter == "u":
        return 2
    if estado_anterior == 2 and caracter == "n":
        return 3

    
    return TRAMPA

#automata fun
def a_fun(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_fun(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("fun", RESULTADO_ACEPTADO),
    ("fu", RESULTADO_NO_ACEPTADO),
    ("function", RESULTADO_TRAMPA),
    ("fun ", RESULTADO_TRAMPA),
    ("ff", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_fun(cadena)))
    assert a_fun(cadena) == resultado