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
		return TRAMPA
	return ACEPTADO
	
def Digito(caracter):
	if not caracter in Digitos or len(caracter) == 0:  
		return TRAMPA
	return ACEPTADO

def ListaSimbolos(cadena):
	for caracter in cadena:
		if Letra(caracter) == TRAMPA and Digito(caracter) == TRAMPA:
			return TRAMPA
	if len(cadena) == 0:
		return TRAMPA
	return ACEPTADO


###########################################################
#las 2 funciones de abajo son para no repetir el codigo en la funcion lexer(cadena)
#
#
#Es necesario que los a_etcetera(cadena) esten en este mismo codigo para que esto funcione
#Tambien es necesario completar los a_etcetera(cadena) == TRAMPA/ACEPTADO aca abajo para completar el lexer
#
#
###########################################################

#Es necesario para saber si llegue a un estado de TRAMPA en todas las posibilidades de la cadena
def TodoTrampa(cadena): 
	if(a_eof(cadena) == TRAMPA and
		a_if(cadena) == TRAMPA and
		a_else(cadena) == TRAMPA and
		##########mas automatas a agregar
		
		ListaSimbolos(cadena) == TRAMPA):
			return True
      
def TipoCadena(cadena):
	if a_eof(cadena) == ACEPTADO:
		tipo = "_EOF"
	elif a_if(cadena) == ACEPTADO:
		tipo = "_IF"
	elif a_else(cadena) == ACEPTADO:
		tipo = "_ELSE"
	#########mas automatas a agregar
	
	else:
		tipo = "ID"
	
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
