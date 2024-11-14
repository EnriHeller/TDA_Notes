# "somos todos montiel. gonzalo, vamos. montiel al arcooooo... argentina campeon del mundo."

from collections import Counter
import heapq

# Calcular frecuencias de cada caracter en el texto
def calcular_frecuencias(texto):
    return dict(Counter(texto))

# Crear un heap vacío
def heap_crear():
    return []

# Clase para representar una hoja en el árbol de Huffman
class Hoja:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia

    # Comparador para el heap
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

# Clase para representar un nodo intermedio en el árbol de Huffman
class Arbol:
    def __init__(self, izq, der, frecuencia):
        self.izq = izq
        self.der = der
        self.frecuencia = frecuencia

    # Comparador para el heap
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

# Codificación Huffman
def codificar(nodo, codigo='', codigos={}):
    if isinstance(nodo, Hoja):
        codigos[nodo.caracter] = codigo
    else:
        codificar(nodo.izq, codigo + '0', codigos)
        codificar(nodo.der, codigo + '1', codigos)
    return codigos

# Función principal de Huffman
def huffman(texto):
    frecuencias = calcular_frecuencias(texto)
    q = heap_crear()

    # Insertar hojas en el heap
    for caracter, frecuencia in frecuencias.items():
        heapq.heappush(q, Hoja(caracter, frecuencia))

    # Construir el árbol de Huffman
    while len(q) > 1:
        t1 = heapq.heappop(q)
        t2 = heapq.heappop(q)
        heapq.heappush(q, Arbol(t1, t2, t1.frecuencia + t2.frecuencia))

    # Obtener la raíz del árbol y generar el código
    arbol = heapq.heappop(q)
    codigos = codificar(arbol)

    # Codificar el texto usando los códigos generados
    texto_codificado = ''.join(codigos[caracter] for caracter in texto)
    return texto_codificado, codigos

# Ejemplo de uso
texto = "somos todos montiel. gonzalo, vamos. montiel al arcooooo... argentina campeon del mundo."
texto_codificado, codigos = huffman(texto)
print("Texto codificado:", texto_codificado)
print("Codigos:", codigos)
