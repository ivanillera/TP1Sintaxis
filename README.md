## TP1Sintaxis

### Por ahora el lexer devuelve una prueba, por ejemplo:

`lexer("if ifno ifyes")`


![xd](https://i.snag.gy/hNBtSR.jpg)

Motivo: Hacer un caso de pruebas con listas es innecesariamente complicado.

## Errores conocidos:

- Meter un simbolo desconocido hace que el lexer tome la subcadena como trampa, haciendo que saltee ese simbolo y siga con otra subcadena

![xd2](https://i.snag.gy/xQrl82.jpg)

Posibles Soluciones:
- Agregar simbolos desconocidos al lexer (como $,%,&,etc)
- Terminar de procesar la subcadena cuando se encuentre un espacio (Creo que no es el objetivo de este tp)
- Hacer que la siguiente subcadena empieze donde se encontraron todos estados trampa, dando como salida las 3 subcadenas: da $ eof (cp-ejemplo de la imagen)
