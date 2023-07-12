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
# fib.append(fib[-1] + fib[-2]) -> no entiendo esta linea

# Ejemplo para entender todo mejor:
fruits = ["apple", "banana", "cherry"]

def probando(n):
 while len(fruits) < n:
  fruits.append("oranges")
 return(fruits)
 
print(probando(7))

'''16. **Ejercicio:** Define una función que tome una lista de números y retorne el número más grande de la lista.'''
def maximo(lista):
    return max(lista)
print(maximo([1, 3, 7, 2, 5]))
#este es fácil

'''17. **Ejercicio:** Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
'''
def suma_cubos_digitos(n):
    return sum(int(digit)**3 for digit in str(n))
print(suma_cubos_digitos(123))

#bucle for recorre el valor de n, que es 123. 1a vuelta -> obtiene 1, lo transforma en int y multiplica 1**3 = 1. 2a vuelta ->obtiene 2, lo transforma en int y multiplica 2**3 = 8. 3a vuelta -> obtiene 3, lo transforma en int y multiplica 3**3 = 27. Finalmente se suma todo 1+8+27 = 36

#Duda: se parece a una duda que tenia antes. Por qué no coge 123 de golpe y los separa? es porque sum() es una funcion dedicada para listas y automaticamente crea una?

'''18. **Ejercicio:** Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.'''
def segundo_maximo(lista):
    return sorted(set(lista), reverse=True)[1]
print(segundo_maximo([1, 3, 7, 7, 2, 5]))

# Hemos indicado 2 parámetros para sorted(). El 1er parámetro y obligatorio es el "iterable", que indica sobre qué elemento se ejecuta la función sorted. En este caso sobre el argumento/parámetro "lista", que a su vez está encerrado en el método set(). Set() crea un objeto de tipo set, una de las caracteristicas de los set es que no permite duplicados. El 2º parámetro indicado es el "reverse" que se indica mediante un booleano. Cuando es True los objetos se ordenan de forma descendente. El 3er parámetro sería "key" pero no está indicado así que por defecto es "none". -> el resultado de esto sería [7,5,3,2,1] -> descendente y sin el duplicado
#[1] hace referencia a la posición 1 de [7,5,3,2,1], es decir, el 5 -> que es el segundo más alto/grande


'''19. **Ejercicio:** Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.'''
def tienen_comun(lista1, lista2):
    return bool(set(lista1) & set(lista2))
print(tienen_comun([1, 2, 3], [3, 4, 5]))

# se parece mucho al ejer.10 pero en este caso devuelve un boolean.

# Dudas: The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0 -> need explanation please

'''20. **Ejercicio:** Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.'''
def invertir_lista(lista):
    return lista[::-1]
print(invertir_lista([1, 2, 3, 4, 5]))

# concepto igual que el ejercicio 6. Si pongo ::1 la lista se queda igual. Si pongo :-1 la lista imprime solo del 1 al 4.

'''21. **Ejercicio:** Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.'''
def contar_digitos_letras(cadena):
    digitos = sum(c.isdigit() for c in cadena)
    letras = sum(c.isalpha() for c in cadena)
    return digitos, letras
print(contar_digitos_letras("Python 3.8"))
# definimos una función, esta función contiene dos variables que hemos llamado dígitos y letras.
#digitos es igual a la suma del bucle for que recorre la cadena ("Python 3.8") y devuelve su resultado y le aplica la función isdigit() -> method returns True if all the characters are digits, otherwise False. (funciona igual para letras con isalpha())
# Entonces supongo que (esta duda la tengo que confirmar) sum() convierte a lista la cadena y pasa letra por letra, y digito por digito, y indigit() o isalpha() va devolviendo solo los que son True? y como solo tenemos los True que o bien serán letras o bien dígitos, los sumará y dara el resltado correcto -> 2 digitos, 6 letras (símbolo "." no cuenta como ninguno de los dos)

#Dudas: repasar que lo que creo que es sea cierto
