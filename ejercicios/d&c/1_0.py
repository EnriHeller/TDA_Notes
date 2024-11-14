def indice_primer_cero(arr):
    buscar_cero(arr, 0, len(arr)-1)

def buscar_cero(arr, inicio, fin):

    if inicio > fin:
        return -1
    
    medio = (inicio + fin) // 2
    
    if arr[medio] == 0 and (medio == 0 or arr[medio - 1] == 1):
        return medio
    
    if arr[medio] == 1:
        return buscar_cero(arr, medio + 1, fin)
    else:
        return buscar_cero(arr, inicio, medio - 1)
        
    return medio