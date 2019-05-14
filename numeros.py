TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#delta Números
def d_num(estado_anterior, caracter):
    if estado_anterior == 0 and caracter in digits:
        return 1
    if estado_anterior == 1 and caracter in digits:
        return 1
    if estado_anterior == 1 and caracter == ".":
        return 2
    if estado_anterior == 2 and caracter in digits:
        return 3
    if estado_anterior == 3 and caracter in digits:
        return 3

    
    return TRAMPA

#automata Numeros
def a_num(cadena):
    Finales = [1, 3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_num(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casos = [
    ("13", RESULTADO_ACEPTADO),
    ("2.69a8", RESULTADO_TRAMPA),
    ("1323234.3", RESULTADO_ACEPTADO),
    ("2522.9.99", RESULTADO_TRAMPA),
    (".0111", RESULTADO_TRAMPA),
    ("1.0000003", RESULTADO_ACEPTADO),
    ("1", RESULTADO_ACEPTADO)
]

for cadena, resultado in casos:
    print((cadena, a_num(cadena)))
    assert a_num(cadena) == resultado