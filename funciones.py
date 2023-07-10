'''
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.
'''

#1
def ejemplosuma(a, b):
    return a + b
suma = ejemplosuma(1,1)
print(suma)

#2
z = 7
def factorial(d):
    if d>0:
        d = d * factorial(d-1)
    else:
        d = 1
    return d
fact1 = factorial(z)
print(fact1)

#3
#4
def lista(listanumeros):
    suma = 0
    for numero in listanumeros:
        suma = suma + numero
    return suma
la_lista = [100,7,22,4,66]
print(lista(la_lista))

#5
def cadena_reversa(cadena):
    return cadena[::-1]
print(cadena_reversa('Mi gata se llama Pipas'))