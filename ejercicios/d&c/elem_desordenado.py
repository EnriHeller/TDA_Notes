def elemento_desordenado(arr):
    return busqueda_binaria(arr, 0, len(arr) - 1)

def busqueda_binaria(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio]
    
    medio = (inicio + fin) // 2
    
    if (medio > 0 and arr[medio] < arr[medio - 1]) or (medio < len(arr) - 1 and arr[medio] > arr[medio + 1]):
        return arr[medio]
    
    if (medio > 0 and arr[medio] < arr[medio - 1]):
        return busqueda_binaria(arr, inicio, medio - 1)
    
    return busqueda_binaria(arr, medio + 1, fin)