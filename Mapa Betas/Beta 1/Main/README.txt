Intrucciones para crear una etapa:

Se debe crear una matriz de 32 * 48, cada celda ocupa un espacio de 32 x 32 pixeles en la pantalla.
En la pantalla se ve una matriz de 32*24, pero se usan mas para colocar trampas ocultas (ver niveles 2 y 4).

Botones y lo que representan:

m = muro (o plataforma)
o = enemigo1
p = enemigo 2
j = jefe
1,2,3,4 = espina que sube,baja,izquierda,derecha
5,6,7,8 = espina quieta arriba,abajo,izquierda,derecha
A,S,D,F = manzana que sube,baja,izquierda,derecha
n = manzana quieta
c = camaespina
s = save (1 por etapa)
f = coneccion con siguiente o anterior etapa
o = ombudsman (1 por etapa)
p = nube (maneja las imagenes correspondientes automaticamente)
a = arbol
P = texto flotante

El texto flotante que aparece en la posicion P, debe estar escrito al final de la fila correspondiente
(ver level 1)

NOTA:

La coneccion con otras etapas sirve solo para la etapa anterior o siguiente. Para reconocerlo, se debe 
situar el "f" en la misma columna o fila de la matriz (ver los que ya estan implementados).
Para agregar otra etapa, en el Main agregar Mapa.append(Clases.Mapa(directorio del archivo, nº de etapa))
El nº de etapa siempre debe ser uno mayor al anterior.

BUGS:

Si encontramos esta situacion:

m
nm

Donde n es Novatin y m son plataformas, saltando y moviendose a la derecha puede atravesarlos (bug no importante)

SOBRE EL SISTEMA DE SAVE

El archivo Password.py posee una clase que no está siendo utilizada y que solo guarda valores. La gracia de esa clase
era simplificar el codigo, cosa que no pude hacer, te lo encargo Eduardo. Si no se hace, da lo mismo xd
Pero la gracia de haberlo echo es que podríamos tirarle una variable 'visible' que sea un boolean que pase
a True al cumplir cierta condición del mapa (x ejemplo, que ya no queden enemigos). Eso :P

NOTA: Mainjoy.py es para jugar con joystick, Main común y corriente, es el de siempre.