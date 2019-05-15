TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


###########################################################
#AUTOMATAS A_ALGO() D_ALGO()
###########################################################








	
###########################################################
#Lo de abajo es necesario para este codigo
#Uso esto para encontrar ESTADO TRAMPA cuando hay un espacio
###########################################################

Digitos = ["0","1","2","3","4","5","6","7","8","9"]

Letras = []
for x in range(97,123):
	Letras.append(chr(x))
for x in range(65,91):
	Letras.append(chr(x))

def Letra(caracter):
	if not caracter in Letras or len(caracter) == 0:
		return RESULTADO_TRAMPA
	return RESULTADO_ACEPTADO
	
def Digito(caracter):
	if not caracter in Digitos or len(caracter) == 0:  
		return RESULTADO_TRAMPA
	return RESULTADO_ACEPTADO

def ListaSimbolos(cadena):
	for caracter in cadena:
		if Letra(caracter) == RESULTADO_TRAMPA and Digito(caracter) == RESULTADO_TRAMPA:
			return RESULTADO_TRAMPA
	if len(cadena) == 0:
		return RESULTADO_TRAMPA
	return RESULTADO_ACEPTADO


###########################################################
#las 2 funciones de abajo son para no repetir el codigo en la funcion lexer(cadena)
###########################################################

#Es necesario para saber si llegue a un estado de TRAMPA en todas las posibilidades de la cadena
def TodoTrampa(cadena): 
	if(a_eof(cadena) == RESULTADO_TRAMPA and
		a_if(cadena) == RESULTADO_TRAMPA and
		a_else(cadena) == RESULTADO_TRAMPA and
		##########mas automatas a agregar
		
		ListaSimbolos(cadena) == RESULTADO_TRAMPA):
			return True
      
def TipoCadena(cadena):
	if a_eof(cadena) == RESULTADO_ACEPTADO:
		tipo = "_EOF"
	elif a_if(cadena) == RESULTADO_ACEPTADO:
		tipo = "_IF"
	elif a_else(cadena) == RESULTADO_ACEPTADO:
		tipo = "_ELSE"
	#########mas automatas a agregar junto con su tipo
	
	else:
		tipo = "TIPO"
	
	return tipo


###################################
#Lexer: voy agarrando elementos de la cadena hasta llegar a un estado trampa.
#Luego volviendo al estado anterior de la cadena, elijo su tipo(if, nombre de variable/texto) segun su prioridad
###################################


def lexer(cadena):
	token = []
	tipo = "ID"
	primerElemento = 0
	ultimoElemento = 0
	
	while ultimoElemento != len(cadena):
		ultimoElemento += 1
		subcadena = cadena[primerElemento:ultimoElemento]
		
		if TodoTrampa(subcadena):
				
			subcadena = cadena[primerElemento:ultimoElemento-1]
			tipo = TipoCadena(subcadena)

			token.append((tipo,subcadena))
			primerElemento = ultimoElemento 
				
		if ultimoElemento == len(cadena):
			tipo = TipoCadena(subcadena)
			token.append((tipo,subcadena))
	#return token
	print(token)
