'''22. **Ejercicio:** Define una función que reciba una lista de números y retorne la sum
a acumulada de los números'''
def suma_acumulada(lista):
    total = 0
    suma_acumulada = []
    for numero in lista:
        total += numero
        suma_acumulada.append(total)
    return suma_acumulada
print(suma_acumulada([1, 2, 3, 4, 5]))

'''23. **Ejercicio:** Define una función que encuentre el elemento más común en una lista.'''
from collections import Counter
def elemento_mas_comun(lista):
    return Counter(lista).most_common(1)[0][0]
print(elemento_mas_comun([1, 2, 3, 2, 4, 2, 5]))

'''24. **Ejercicio:** Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.'''
def tabla_de_multiplicar(numero):
    return {i: numero * i for i in range(1, 11)}
print(tabla_de_multiplicar(5))

'''25. **Ejercicio:** Define una función que tome una cadena y retorne un diccionario con
la cantidad de apariciones de cada caracter en la cadena.'''
def contar_caracteres(cadena):
    return {caracter: cadena.count(caracter) for caracter in cadena}
print(contar_caracteres("hola hola"))

'''26. **Ejercicio:** Define una función que tome dos listas y retorne la lista de elemen
tos que no están en ambas listas.
'''
def elementos_no_comunes(lista1, lista2):
    return list(set(lista1) ^ set(lista2))
print(elementos_no_comunes([1, 2, 3, 4], [3, 4, 5, 6]))

'''27. **Ejercicio:** Define una función que tome una lista y retorne la lista sin duplic
Resolución & Entrega de ejercicios 11
ados.'''
def eliminar_duplicados(lista):
    return list(set(lista))
print(eliminar_duplicados([1, 2, 2, 3, 4, 4]))

'''28. **Ejercicio:** Define una función que reciba un número entero positivo y retorne l
a suma de los cuadrados de todos los números pares menores o iguales a ese número.'''
def suma_cuadrados_pares(n):
    return sum(i**2 for i in range(2, n+1, 2))
print(suma_cuadrados_pares(6))