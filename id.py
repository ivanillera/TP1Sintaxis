TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
"u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", 
"F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", 
"U", "V", "W", "X", "Y", "Z"]

#delta ID
def d_id(estado_anterior, caracter):
    if estado_anterior == 0 and caracter in letras:
        return 1
    if estado_anterior == 1 and caracter in letras:
        return 1
    if estado_anterior == 1 and caracter in digits:
        return 1

    
    return TRAMPA

#automata ID
def a_id(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_id(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casos = [
    ("hola1", RESULTADO_ACEPTADO),
    ("hola", RESULTADO_ACEPTADO),
    ("1", RESULTADO_TRAMPA)
]

for cadena, resultado in casos:
    print((cadena, a_id(cadena)))
    assert a_id(cadena) == resultado

