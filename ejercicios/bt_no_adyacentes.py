"""
Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V, devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.
"""

def no_adyacentes(grafo, n):
    'Devolver una lista con los n vértices, o None de no ser posible'
    vertices = grafo.obtener_vertices()
    rec_no_adyacentes(grafo, vertices,0,[],n)

def es_compatible(grafo, res, nuevo_v):
    for w in res:
        if grafo.estan_unidos(nuevo_v, w):
            return False
    
    return True

def rec_no_adyacentes(grafo,vertices, v, res, n):

    #Si la respuesta construida coincide con la cantidad de vertices que quiero devolver, retorno respuesta
    if len(res) == n: 
        return es_compatible(grafo, res, v)

    #Si ya llegué al largo del grafo, me pasé y no existe un independent set
    if v == len(vertices): 
        return False
    

    #¿Lo que hice hasta acá es compatible?, Si no lo es cortá.
    if not es_compatible(grafo, res, vertices[v]):
        return False
    
    #Si llego hasta acá, el vertice actual es valido para incorporar a la respuesta 
    res.add(vertices[v])

    #Sigo recorriendo habiendo añadido este vertice
    if rec_no_adyacentes(grafo,vertices,v+1,res,n):
        return True

    #Si llegué hasta acá es que habiendo añadido este vertice no llego a una respuesta valida, entonces lo saco. 
    res.remove(vertices[v])

    #Vuelvo a intentar habiendo sacado ese vertice. 
    return rec_no_adyacentes(grafo,vertices,v+1,res, n)