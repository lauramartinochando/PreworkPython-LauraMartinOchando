''' 8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3. '''

def es_perfecto(num):
    return num == sum(divisor for divisor in range(1, num) if num % divisor == 0)
print(es_perfecto(6))

# == es lo que nos devuelve True o False: Comprueba que el resultado de la suma sea exactamente al valor de "num", osea 6. Creamos un bucle for que recorre el range que empieza en 1 y terminará en 6. 1a vuelta -> 1. Es el resto de 6/1 igual a 0? sí (1 es True, nos lo quedamos). 2a vuelta-> 2. Es el resto de 6/2 igual a 0? sí (True, nos vale). 3a vuelta -> 3.Es el resto de 6/3 igual a 0? True. 4a vuelta -> 4.Es el resto de 6/4 igual a 0? no (False, 4 no nos vale). 5a vuelta -> 5. Es el resto de 6/5 igual a 0? False. 6a y última vuelta -> 6.Es el resto de 6/6 igual a 0? True.
# Un vez finalizado el bucle sumamos los números que son True -> 1 + 2 + 3 = 6 -> 6 es un número perfecto

#Duda: si el fin del bucle son 6 vueltas, la sexta vuelta entra en el bucle o para en la 5a?

'''9. Ejercicio: Define una función que reciba un número y retorne su representación
en binario.'''
def a_binario(n):
    return bin(n).replace("0b", "")
print(a_binario(36))
# bin() es una funcion predeterminada que devuelve el binario de cualquier número, en este caso de 36. Aparte de esto, aquí estamos reemplazando 0b por " " para quitar el 0b del resultado ya que la funcion bin() siempre lo añade al principio. 0b100100 pasa a ser 100100.

'''10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).
'''
def interseccion(list1, list2):
    return list(set(list1) & set(list2))
print(interseccion([1, 2, 3, 4], [3, 4, 5, 6]))

# la funcion list() crea un objeto tipo lista. Dentro de la función list también tenemos dos funciones set(), que crea un objeto tipo set. Vale pero qué hace que se escojan solo los que coinciden? -> los sets no guardan valores duplicados.

# Dudas: The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0 -> need explanation please

'''11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''
def es_palindromo(cadena):
    return cadena == cadena[::-1]
print(es_palindromo("radar"))

#se entiende fácil usando :: que lo hemos explicado antes

'''12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”.
'''
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
# range empieza su bucle por el nº1 y para en el nº50. Simplemente metemos una condición por cada caso usando if/elif y sabemos si son divisores de 3/5 siempre y cuando el resto de la división sea 0.

'''13. **Ejercicio:** Define una función que tome una lista y retorne la lista ordenada en orden ascendente.'''
def ordenar_lista(lista):
    return sorted(lista)
print(ordenar_lista([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
# sintaxis de la funcion sorted() -> sorted(iterable, key=key, reverse=reverse). iterable (Required) -> The sequence to sort, list, dictionary, tuple etc. key (Optional) -> A Function to execute to decide the order. Default is None. revers (Optional) -> A Boolean. False will sort ascending, True will sort descending. Default is False. En este caso como no hemos indicado nada por defecto lo ordena ascendentemente.

'''14. **Ejercicio:** Define una función que reciba una lista de palabras y un entero n,
y retorne la lista de palabras que son más largas que n.'''
def filtrar_palabras(lista_de_palabras, n):
    return [palabra for palabra in lista_de_palabras if len(palabra) > n]
print(filtrar_palabras(["hola", "mundo", "python", "programacion"], 5))

# Recorremos la lista_de_palabras y nos devuelve la misma lista pero solo de los elementos que cumplen la condicion if -> que la longitud de la palabra sea estrictamente mayor que 5.

#también podemos hacer esto usando la función list():
def filtrar_palabras(lista_de_palabras, n):
    return list(palabra for palabra in lista_de_palabras if len(palabra) > n)
print(filtrar_palabras(["hola", "mundo", "python", "programacion"], 5))



