def contar_inversiones(A, B):

    _, inversiones = merge_sort(B)
    return inversiones


def merge_sort(arr):

    if len(arr) <= 1:
        return arr, 0

    medio = (len(arr) // 2)

    izq, invIzq = merge_sort(arr[:medio])
    der, invDer = merge_sort(arr[medio:])

    arreglo, invFinal = merge(izq, der)
    return arreglo, (invFinal + invIzq + invDer)

def merge(arr1, arr2):
    res = []

    i1 = 0
    i2 = 0

    inversiones = 0
    
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] <= arr2[i2]:
            res.append(arr1[i1])
            i1 += 1
        else:
            res.append(arr2[i2])
            i2 += 1
            inversiones += (len(arr1) - i1)

    while i1 < len(arr1):
        res.append(arr1[i1])
        i1 += 1

    while i2 < len(arr2):
        res.append(arr2[i2])
        i2 += 1
    
    return res, inversiones