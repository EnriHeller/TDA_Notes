def multiplicar(a, b):
    
    n = max(len(str(a)), len(str(b)))
    n_half = n // 2
    a1,a2 = divmod(a, 10**n_half)
    b1,b2 = divmod(b, 10**n_half)

    z0 = multiplicar(a1,b1)
    z1 = multiplicar((a1+a2), (b1+b2))
    z2 = multiplicar(a2, b2)

    return (z2 * 10**(2 * n_half)) + ((z1 - z2 - z0) * 10**n_half) + z0

