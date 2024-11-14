def indice_mas_bajo(alumnos):

    if len(alumnos) == 1:
        return 0
    

    medio = int(len(alumnos/2))

    if validar_mas_bajo(alumnos, medio):
        return medio
    
    izq = indice_mas_bajo[:medio]
    der = indice_mas_bajo[medio:]

    

def validar_mas_bajo(alumnos, indice):

    if indice > 0 and indice < len(alumnos) - 1:
        return alumnos[indice].altura < alumnos[indice - 1].altura and alumnos[indice].altura < alumnos[indice + 1].altura
    elif indice == 0:
        return alumnos[indice].altura < alumnos[indice + 1].altura
    elif indice == len(alumnos) - 1:
        return alumnos[indice].altura < alumnos[indice - 1].altura
    return False

def minimo(arreglo, inicio, fin):

    if inicio >= fin:
        return inicio

    medio = int((inicio+fin) / 2)

    min_izq = minimo(arreglo, inicio, medio)
    min_der = minimo(arreglo, medio + 1, fin)

    if arreglo[min_izq].altura < arreglo[min_der].altura:
        return min_izq

    return min_der

