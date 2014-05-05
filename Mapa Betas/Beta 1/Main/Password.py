caracteres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
seleccion = 1
movil = True
clave = ""
no_repetir = False

def borra_espacio(clave):
    aux = ""
    for j in range(len(clave)-1):
        aux += clave[j]
    return aux

def mover_arriba(seleccion, movil):
    if movil:
        if seleccion > 12:
            seleccion -= 12
        elif seleccion%12 <= 6:
            seleccion = 37
        else:
            seleccion = 38
        movil = False
    else:
        movil = True
    return seleccion, movil

def mover_abajo(seleccion, movil):
    if movil:
        if seleccion <= 24:
            seleccion += 12
        elif seleccion > 36:
            seleccion = 6
        elif seleccion%12 <= 6:
            seleccion = 37
        else:
            seleccion = 38
        movil = False
    else:
        movil = True
    return seleccion, movil

def mover_derecha(seleccion, movil):
    if movil:
        if seleccion <= 36:
            if seleccion%12 == 0:
                seleccion -= 11
            else:
                seleccion += 1
        elif seleccion == 37:
            seleccion = 38
        else:
            seleccion = 37
        movil = False
    else:
        movil = True
    return seleccion, movil

def mover_izquierda(seleccion, movil):
    if movil:
        if seleccion <= 36:
            if seleccion%12 == 1:
                seleccion += 11
            else:
                seleccion -= 1
        elif seleccion == 37:
            seleccion = 38
        else:
            seleccion = 37
        movil = False
    else:
        movil = True
    return seleccion, movil

def posicion_cursor(seleccion):
    if seleccion <= 36:
        x,y = 55+(seleccion-1)%12*80, 185 + (seleccion-1)//12 * 100
    else:
        x,y = 200+(seleccion-37)*300, 565
    return (x,y)

def posicion_teclado(n):
    x,y = 100+n%12*80, 200+n//12*100
    return x,y

def posicion_clave(n):
    x,y = 400+40*n,100
    return x,y
