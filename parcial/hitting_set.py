def verificador(k, c, Bs):
    if len(c) > k:
        return False
    
    for B in Bs:
        contador = 0

        for elem in B:
            if elem in c:
                contador += 1
        
        if contador == 0:
            return False
    
    return True