def invertir_palabras(cadena):
    return ' '.join(cadena.split()[::-1])
print(invertir_palabras("Hola, ¿cómo estás?"))