TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


#delta var
def d_var(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "v":
        return 1
    if estado_anterior == 1 and caracter == "a":
        return 2
    if estado_anterior == 2 and caracter == "r":
        return 3

    
    return TRAMPA

#automata var
def a_var(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_var(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

## PRUEBAS

casos = [
    ("var", RESULTADO_ACEPTADO),
    ("va", RESULTADO_NO_ACEPTADO),
    ("var:", RESULTADO_TRAMPA),
    ("f", RESULTADO_TRAMPA),
    ("123", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_var(cadena)))
    assert a_var(cadena) == resultado