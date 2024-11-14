def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    medio = (len(arr) // 2)

    izq = merge_sort(arr[:medio])
    der = merge_sort(arr[medio:])

    return merge(izq, der)

def merge(arr1, arr2):
    res = []

    i1 = 0
    i2 = 0
    
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] <= arr2[i2]:
            res.append(arr1[i1])
            i1 += 1
        else:
            res.append(arr2[i2])
            i2 += 1

    while i1 < len(arr1):
        res.append(arr1[i1])
        i1 += 1

    while i2 < len(arr2):
        res.append(arr2[i2])
        i2 += 1
    
    return res