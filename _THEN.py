ESTADO_TRAMPA = -1

ACEPTADO = "aceptado"
ERROR = "error"
TRAMPA = "trampa"


def _THEN(cadena):
    aceptados = [4]
    estado = 0
    for c in cadena:
        if estado == 0 and c == 't':
            estado = 1
        elif estado == 1 and c == 'h':
            estado = 2
        elif estado == 2 and c == 'e':
            estado = 3
        elif estado == 3 and c == 'n':
            estado = 4    
        else:
            estado = ESTADO_TRAMPA
            break

    if estado in aceptados:
        return ACEPTADO
    if estado == ESTADO_TRAMPA:
        return TRAMPA
    return ERROR


print(_THEN("then") == ACEPTADO)
print(_THEN("th") == ERROR)
print(_THEN("g") == TRAMPA)
