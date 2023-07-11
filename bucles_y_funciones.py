''' 1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci. '''

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
fibonacci(10)
# range genera una secuencia de nums del 0 al 10. Durante esa iteración se imprimirá el valor de a, 0, y end=" " (que intuyo es un espacio en blanco entre num y num.)-> 0 + " " en la 1a vuelta. Después cambian los valores de las variables, a pasa a tener el valor de 1 y b pasa a ser 0 + 1, o sea, 1. Empezamos 2a vuelta-> a=1 y b=1, iteramos e imprimimos print(1, " "). Valores cambian, ahora a=1 (otra vez) y b vale 2 (1+1). 3a vuelta -> a=1 y b=2. Iteramos e imprimimos print(1, " ") y cambian los valores: ahora a=2 y b=3 (1+2). 4a vuelta -> a=2,b=3, iteramos e imprimimos (2, " ") y cambian valores, ahora a=3 y b=5(2+3). Empezamos 5a vuelta -> iteramos e imprimimos print(3, " ") y cambian valores, ahora a = 5 y b=8(3+5). 6a vuelta, iteramos e imprimimos print(5, " ") y cambian valores...etc

'''2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores. '''
def divisores(a):
    for i in range(1, a+1):
        if a % i == 0:
            return i
print(divisores)

#2 solucion
def divisores(n):
    return [i for i in range(1, n + 1) if n % i == 0]
print(divisores(12))

'''3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.'''
def nuevaLista(lista1):
    return list(set(lista1))
print(nuevaLista(['Carol', 'Laura', 'Pilar', 'Sergio', 'Laura', 'Pilar']))

'''4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.'''
def suma_digitos(n):
    return sum(int(digito) for digito in str(n))
print(suma_digitos(123))

'''5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.'''
def contar_vocales(cadena):
    return sum(1 for letra in cadena if letra.lower() in 'aeiou')
print(contar_vocales('Hola Mundo'))

'''6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista. '''
def elementos(list, n):
    return list[:n]
print(elementos([1,2,3,4,5,6],3))

''' 7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena. '''
def fcadena(cadena):
    mayusculas = sum(1 for letra in cadena if letra.isupper())
    minusculas = sum(1 for letra in cadena if letra.islower())
    return mayusculas, minusculas
print(fcadena("Me llamo Laura"))

''' 8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3. '''

def es_perfecto(num):
    return num == sum(divisor for divisor in range(1, num) if num % divisor == 0)
print(es_perfecto(6))

# == es lo que nos devuelve True o False
#range genera una secuencia de números. Aqui va del 1 al 6 -> no se ha explicado en ningún sitio menos los apuntes y solo con 1 parametro ?? (w3schools start,stop,step)
#divisor no lo entiendo, por qué aparece el nombre divisor antes y despues de "for"?

'''9. Ejercicio: Define una función que reciba un número y retorne su representación
en binario.'''
def a_binario(n):
    return bin(n).replace("0b", "")
print(a_binario(5))
#reemplazamos 0b por " " para quitar el 0b ya que siempre sale x defecto

'''10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).
'''
def interseccion(list1, list2):
    return list(set(list1) & set(list2))
print(interseccion([1, 2, 3, 4], [3, 4, 5, 6]))

'''11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''
def es_palindromo(cadena):
    return cadena == cadena[::-1]
print(es_palindromo("radar"))

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

'''13. **Ejercicio:** Define una función que tome una lista y retorne la lista ordenada e
n orden ascendente.'''
def ordenar_lista(lista):
    return sorted(lista)
print(ordenar_lista([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

'''14. **Ejercicio:** Define una función que reciba una lista de palabras y un entero n,
y retorne la lista de palabras que son más largas que n.'''
def filtrar_palabras(lista_de_palabras, n):
    return [palabra for palabra in lista_de_palabras if len(palabra) > n]
print(filtrar_palabras(["hola", "mundo", "python", "programacion"], 5))

'''15. **Ejercicio:** Define una función que tome un número y calcule su serie de Fibonac
ci.'''
def serie_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
print(serie_fibonacci(10))

'''16. **Ejercicio:** Define una función que tome una lista de números y retorne el númer
o más grande de la lista.'''
def maximo(lista):
    return max(lista)
print(maximo([1, 3, 7, 2, 5]))

'''17. **Ejercicio:** Define una función que reciba un número y retorne la suma de sus dí
gitos al cubo.
'''
def suma_cubos_digitos(n):
    return sum(int(digit)**3 for digit in str(n))
print(suma_cubos_digitos(123))

'''18. **Ejercicio:** Define una función que reciba una lista de números y retorne el seg
undo número más grande de la lista.'''
def segundo_maximo(lista):
    return sorted(set(lista), reverse=True)[1]
print(segundo_maximo([1, 3, 7, 7, 2, 5]))

'''19. **Ejercicio:** Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.'''
def tienen_comun(lista1, lista2):
    return bool(set(lista1) & set(lista2))
print(tienen_comun([1, 2, 3], [3, 4, 5]))

'''20. **Ejercicio:** Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.'''
def invertir_lista(lista):
    return lista[::-1]
print(invertir_lista([1, 2, 3, 4, 5]))

'''21. **Ejercicio:** Define una función que reciba una cadena y cuente el número de dígi
tos y letras que contiene.
'''
def contar_digitos_letras(cadena):
    digitos = sum(c.isdigit() for c in cadena)
    letras = sum(c.isalpha() for c in cadena)
    return digitos, letras
print(contar_digitos_letras("Python 3.8"))

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


