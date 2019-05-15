ESTADO_TRAMPA = -1

ACEPTADO = "aceptado"
ERROR = "error"
TRAMPA = "trampa"


def a_if(cadena):
    aceptados = [2]
    estado = 0
    for c in cadena:
        if estado == 0 and c == 'i':
            estado = 1
        elif estado == 1 and c == 'f':
            estado = 2
        else:
            estado = ESTADO_TRAMPA
            break

    if estado in aceptados:
        return ACEPTADO
    if estado == ESTADO_TRAMPA:
        return TRAMPA
    return ERROR


assert(a_if("if") == ACEPTADO)
assert(a_if("i") == ERROR)
assert(a_if("j") == TRAMPA)
