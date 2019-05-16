TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"


###########################################################
#AUTOMATAS A_ALGO() D_ALGO()
###########################################################








	
###########################################################
#Lo de abajo es necesario para este codigo
#Uso esto para encontrar ESTADO TRAMPA cuando no se encuentran ni digitos ni letras. 
#(Creo que no debemos buscar " " para reconocer palabras porque no seria el objetivo del tp)
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
#Luego del estado trampa tomo la cadena antes de llegar al estado trampa, examino lo que tengo y devuelvo una lista con: (tipo, cosa leida).
###################################


def lexer(cadena):
	token = []
	tipo = ""
	primerElemento = 0
	ultimoElemento = 0
	
	#Repetimos esto hasta leer toda la cadena
	while ultimoElemento != len(cadena):
		ultimoElemento += 1
		subcadena = cadena[primerElemento:ultimoElemento]
		
		#examino si lo que leo es trampa en todos los automatas
		if TodoTrampa(subcadena):
			#al ser todo trampa, examino lo que es por prioridad, dsp guardo lo leido y su tipo en una lista
			subcadena = cadena[primerElemento:ultimoElemento-1]
			tipo = TipoCadena(subcadena)
			token.append((tipo,subcadena))
			
			primerElemento = ultimoElemento 
				
		#Esto es lo mismo que arriba porque por alguna razon no pude hacer que la ultma palabra sea examinada por el algoritmo anterior, asi que lo hago aca
		if ultimoElemento == len(cadena):
			tipo = TipoCadena(subcadena)
			token.append((tipo,subcadena))

	#return token
	print(token)
