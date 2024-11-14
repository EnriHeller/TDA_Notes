def indice_mas_bajo(alumnos):
    return buscar_indice(alumnos, 0, len(alumnos)-1)

def buscar_indice(alumnos, inicio, fin):
    if inicio == fin:
        return inicio

    medio = (inicio + fin) // 2

    if validar_mas_bajo(alumnos, medio):
        return medio
    if alumnos[medio - 1].altura < alumnos[medio].altura:
        return indice_mas_bajo(alumnos, inicio, medio)
    else:
        return indice_mas_bajo(alumnos, medio + 1, fin)

def validar_mas_bajo(alumnos, indice):
    if indice > 0 and indice < len(alumnos) - 1:
        return alumnos[indice].altura < alumnos[indice - 1].altura and alumnos[indice].altura < alumnos[indice + 1].altura
    elif indice == 0:
        return alumnos[indice].altura < alumnos[indice + 1].altura
    elif indice == len(alumnos) - 1:
        return alumnos[indice].altura < alumnos[indice - 1].altura
    return False
