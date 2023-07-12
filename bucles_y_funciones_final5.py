'''29. **Ejercicio:** Define una función que reciba una lista de números y retorne el pro
medio de los números en la lista.'''
def promedio(lista):
    return sum(lista) / len(lista)
print(promedio([1, 2, 3, 4, 5]))

'''30. **Ejercicio:** Define una función que reciba una lista de cadenas y retorne la cad
ena más larga en la lista.
'''
def cadena_mas_larga(lista):
    return max(lista, key=len)
print(cadena_mas_larga(["hola", "mundo", "python"]))

'''31. Ejercicio: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos.'''
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True
        
def primeros_n_primos(n):
    primos = []
    numero = 2
    while len(primos) < n:
        if es_primo(numero):
            primos.append(numero)
    numero += 1
    return primos
print(primeros_n_primos(5))

'''32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.'''
def invertir_palabras(cadena):
    return ' '.join(cadena.split()[::-1])
print(invertir_palabras("Hola, ¿cómo estás?"))

'''33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.
'''
def ordenar_por_ultimo_elemento(tuplas):
    return sorted(tuplas, key=lambda x: x[-1])
print(ordenar_por_ultimo_elemento([(1, 2), (3, 1), (4, 5)]))

'''34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.
'''
def contar_vocales(cadena):
    return sum(1 for c in cadena.lower() if c in 'aeiou')
print(contar_vocales("Hola Mundo"))

'''35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.'''
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(es_primo(17))