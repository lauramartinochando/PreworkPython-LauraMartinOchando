'''1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci.
2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores.
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.
4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.
5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.'''

#1
#2
def divisores(a):
    for i in range(1, a+1):
        if a % i == 0:
            return i
print(divisores)

#3
def nuevaLista(lista1):
    return list(set(lista1))
print(nuevaLista(['Carol', 'Laura', 'Pilar', 'Sergio', 'Laura', 'Pilar']))

#4
#5
'''
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.
7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.
8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario.
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).'''

#6
def elementos(list, n):
    return list[:n]
print(elementos([1,2,3,4,5,6],3))

#7
def fcadena(cadena):
    mayusculas = sum(1 for letra in cadena if letra.isupper())
    minusculas = sum(1 for letra in cadena if letra.islower())
    return mayusculas, minusculas
print(fcadena("Me llamo Laura"))

    
