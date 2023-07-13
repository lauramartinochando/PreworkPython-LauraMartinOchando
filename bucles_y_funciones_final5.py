'''29. **Ejercicio:** Define una función que reciba una lista de números y retorne el promedio de los números en la lista.'''
def promedio(lista):
    return sum(lista) / len(lista)
print(promedio([1, 2, 3, 4, 5]))

#la suma de 1+2+3+4+5 = 15 / el nº total de objetos en la lista: 5 -> 15/5=3. El promedio es 3

'''30. **Ejercicio:** Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
'''
def cadena_mas_larga(lista):
    return max(lista, key=len)
print(cadena_mas_larga(["hola", "mundo", "python"]))
#max() devuelve el valor más alto (If the values are strings, an alphabetically comparison is done.)

#Dudas: no entendía porqué estaba puesto key=len si la función max() ya tiene en cuenta en contar el núm. de caracteres cuando son strings. Así que he comprobado que si eliminas key=len funciona igual, hay alguna razón por la que se puso?

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

# Dudas: no sé cómo se hace la función "es_primo" que es también el ejercicio 35.

'''32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.'''
def invertir_palabras(cadena):
    return ' '.join(cadena.split()[::-1])
print(invertir_palabras("Hola, ¿cómo estás?"))

# The join() method takes all items in an iterable and joins them into one string. Lo que se pone antes del .join() es lo que tú quieras que separe los elementos. El método split() separa todos los elementos y los mete dentro de una lista (crea una lista) -> en este caso sería ["Hola,", "¿cómo", "estás?"] a este resultado se le aplica el [::-1] que ya hemos visto antes, por lo que se invierte el orden y queda en: "estás? ¿cómo Hola,". El output final ya no está dentro de una lista porque hemos usado join() con el separador " "

'''33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.
'''
def ordenar_por_ultimo_elemento(tuplas):
    return sorted(tuplas, key=lambda x: x[-1])
print(ordenar_por_ultimo_elemento([(1, 2), (3, 1), (4, 5)]))

# (A tuple is a collection which is ordered and unchangeable). Las tuplas se representan entre paréntesis ().
# la función sorted() puede contener 3 parámetros. El primero y obligatorio es indicar qué elemento vamos a ordenar, aquí es "tuplas". El segundo es la key, que indicará el orden. Para este orden hemos usado la función lambda, que toma un argumento (x) y una expresión (x[-1]).

#Dudas: no entiendo la x en el lambda


'''34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.
'''
def contar_vocales(cadena):
    return sum(1 for c in cadena.lower() if c in 'aeiou')
print(contar_vocales("Hola Mundo"))
#igual que el ejer.5? mismas dudas

'''5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.'''
def contar_vocales(cadena):
    return sum(1 for letra in cadena if letra.lower() in 'aeiou')
print(contar_vocales('Hola Mundo'))

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

# Si el num (17) es menor que 2 -> devuelve False (los numeros primos solo pueden ser mayores que 1). Bucle: recorre el range empezando por el número 2. El stop es el número integro de "num" exponenciado a 0.5 (17**0,5) = 4 Y +1 = 5. El step por defecto es de 1 en 1 (por lo que en la siguiente vuelta empezaría por 3)
#Este bucle se retornará False si se cumple la sig. condición: si el resto de "num"(17) / i (osea el resultado del bucle) == 0. 

#Dudas: aquí no entiendo el start point del range para qué sirve si ya hemos indicado que los número menores a 2 no pasan más allá y no veo cómo usar el 2 en la operación si estamos llamando al "num"