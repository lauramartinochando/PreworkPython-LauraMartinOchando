'''15. **Ejercicio:** Define una función que tome un número y calcule su serie de Fibonacci.'''
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

# 1)Si 10 es menor o igual a 0 -> devuelve una lista que no contiene nada. 2)Si 10 es exactamente igual que 1 devuelve una lista que contiene 0. Declaramos la variable "fib" y le damos de valor una lista que contiene el numero 0 y el 1.
# bucle while: mientras la longitud de la lista "fib" sea menor de 10 elementos...

# Dudas: 1a vuelta -> tenemos [0,1] que es menor que 10, así que añadimos [-1] + [-2] = -3. 2a vuelta -> tenemos [0,1,-3] -> no lo entiendo, no deberia añadir -3 todo el rato hasta llegar a 10 elementos?

# Ejemplo para entender todo mejor:
fruits = ["apple", "banana", "cherry"]

def probando(n):
 while len(fruits) < n:
  fruits.append("oranges")
 return(fruits)
 
print(probando(7))

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