Intrucciones para crear una etapa:

Se debe crear una matriz de 32 * 48, cada celda ocupa un espacio de 32 x 32 pixeles en la pantalla.
En la pantalla se ve una matriz de 32*24, pero se usan mas para colocar trampas ocultas (ver niveles 2 y 4).

Botones y lo que representan:

m = muro (o plataforma)
e = enemigo
w = espina que sube
q = espina quieta
l = manzana que sube
k = manzana que baja
n = manzana quieta
c = camaespina
s = save (1 por etapa)
f = coneccion con siguiente o anterior etapa
o = ombudsman (1 por etapa)
p = nube (maneja las imagenes correspondientes automaticamente)
a = arbol

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