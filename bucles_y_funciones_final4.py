'''22. **Ejercicio:** Define una función que reciba una lista de números y retorne la suma acumulada de los números'''
def suma_acumulada(lista):
    total = 0
    suma_acumulada = []
    for numero in lista:
        total += numero
        suma_acumulada.append(total)
    return suma_acumulada
print(suma_acumulada([1, 2, 3, 4, 5]))

# 1a vuelta -> total empieza con 0, a total se le suma el primer valor de la lista que se recoge del bucle "numero". 0+1=1. 2a vuelta -> total ahora tiene el valor de 1, a total se le suma el segundo valor de la lista que se recoge del bucle "numero". 1+2=3. 3a vuelta -> total ahora vale 3, a tota se le suma el tercer valor de la lista que se recoge en el bucle "numero". 3+3=6. 4a vuelta -> total ahora vale 6, a total se le suma el cuarto valor de la lista que se recoge en el bucle "numero". 6+4=10 ... y asi sucesivamente:
# 0+1=1 [1] 1+2=3 [1,3] 3+3=6 [1,3,6] 6+4=10 [1,3,6,10] 10+5=15 [1,3,6,10,15]
# Como vemos en el comentario de arriba, los resultados se van añadiendo a la lista vacía que había en la variable suma_acumulada = []. Se va añadiendo porque hemos usado la función .append(total) -> la variable "total" empieza con 0, pero va cambiando su valor conforme hace la operación de total = total + numero, y numero va cogiendo un número distinto en cada vuelta que da el bucle.

'''23. **Ejercicio:** Define una función que encuentre el elemento más común en una lista.'''
from collections import Counter
def elemento_mas_comun(lista):
    return Counter(lista).most_common(1)[0][0]
print(elemento_mas_comun([1, 2, 3, 2, 4, 2, 5]))

# A Counter is a container that keeps track of how many times equivalent values are added. It can be used to implement the same algorithms for which bag or multiset data structures are commonly used in other languages.
# Counter () command to find the most common list elements in Python. For this, you need to import the Counter class from the collections standard library. A Counter is a collection where elements are stored as dictionary keys, and the key’s counts are stored as dictionary values.
# qué es (1)[0][0] ? puede ser: "it will select the first seen element in case of ties."

# dudas: no me da tiempo a buscar bien, preguntar directamente cómo funciona

'''24. **Ejercicio:** Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.'''
def tabla_de_multiplicar(numero):
    return {i: numero * i for i in range(1, 11)}
print(tabla_de_multiplicar(5))

# los simbolos { } son de un obj tipo diccionario -> con esto creamos el diccionario. (Dictionaries are used to store data values in key:value pairs.) La "i" es el key, y "numero" es el value (el valor de "i" depende del bucle, así que su valor irá cambiando, el valor del número es siempre 5) Así que: 1a vuelta -> empezamos por el 1 -> 1:(5*1) osea 5:1. 2a vuelta -> el siguiente es el 2 -> 2:(5*2) osea 2:10 .3a vuelta -> el siguiente es el 3 -> 2:(5*3) osea 2:15 ... y así sucesivamente hasta el 10, porque en range hemos indicado que pararemos en el 11.

'''25. **Ejercicio:** Define una función que tome una cadena y retorne un diccionario con
la cantidad de apariciones de cada caracter en la cadena.'''
def contar_caracteres(cadena):
    return {caracter: cadena.count(caracter) for caracter in cadena}
print(contar_caracteres("hola hola"))

# la key es "caracter" y "caracter" es el resultado de cada vuelta del bucle sobre el parametro "cadena" (sobre "hola hola") -> pero cadena no es una lista, entonces como sabe python que debe separar cada caracter de la cadena de texto?? "caracter" no es una funcion predeterminada! si le cambiamos el nombre funciona igual!. De cualquier modo, la key caracter en la primera vuelta es "h" y el value será el valor indique la función count() -> es decir, Cuenta el número de elementos que aparece "h" en la cadena (porque count() está unido a cadena). En la 2a vuelta será -> Cuenta el número de elementos que aparece "o" en la cadena, y así sucesivamente.
# (The count() method returns the number of elements with the specified value)

# Dudas: cómo sabe python que debe separar cada caracter de la cadena de texto?? "caracter" no es una funcion predeterminada! si le cambiamos el nombre funciona igual!

'''26. **Ejercicio:** Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
'''
def elementos_no_comunes(lista1, lista2):
    return list(set(lista1) ^ set(lista2))
print(elementos_no_comunes([1, 2, 3, 4], [3, 4, 5, 6]))

#este es como el ejercicio 10 y 19, especialmente el ejer.10. Lo unico que cambia es el simbolo ^, asi que la solucion debe estar ahí.

'''27. **Ejercicio:** Define una función que tome una lista y retorne la lista sin duplicados.'''
def eliminar_duplicados(lista):
    return list(set(lista))
print(eliminar_duplicados([1, 2, 2, 3, 4, 4]))
#la función set() ya se encarga de devolver un objeto set sin duplicados (es una de las características de los set). Por lo que de la lista se toman los números 1,2,3,4 y este set se transforma en lista con la función list()

'''28. **Ejercicio:** Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.'''
def suma_cuadrados_pares(n):
    return sum(i**2 for i in range(2, n+1, 2))
print(suma_cuadrados_pares(6))

# lo que sea que de "i" será multiplicado al cuadrado, e "i" lo conseguimos en el bucle for: rango (empezamos por 2, paramos en n+1 (osea en 7??), e incrementamos cada 2 numeros). 1a vuelta-> 2 ** 2 = 4. 2a vuelta -> (incrementamos 4) 4**2=16. 3a vuelta -> 6**2=36. No hay más vueltas porque si incrementamos 2 más sería 8 y eso esta por encima del n+1 (que es 7). Ahora sumamos todos los resultados: 4+16+36= 56