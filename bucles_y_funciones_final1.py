''' 1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci. '''

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
fibonacci(10)
# range genera una secuencia de nums del 0 al 10. Durante esa iteración se imprimirá el valor de a, 0, y end=" " (que intuyo es un espacio en blanco entre num y num.)-> 0 + " " en la 1a vuelta. Después cambian los valores de las variables, a pasa a tener el valor de 1 y b pasa a ser 0 + 1, o sea, 1. Empezamos 2a vuelta-> a=1 y b=1, iteramos e imprimimos print(1, " "). Valores cambian, ahora a=1 (otra vez) y b vale 2 (1+1). 3a vuelta -> a=1 y b=2. Iteramos e imprimimos print(1, " ") y cambian los valores: ahora a=2 y b=3 (1+2). 4a vuelta -> a=2,b=3, iteramos e imprimimos (2, " ") y cambian valores, ahora a=3 y b=5(2+3). Empezamos 5a vuelta -> iteramos e imprimimos print(3, " ") y cambian valores, ahora a = 5 y b=8(3+5). 6a vuelta, iteramos e imprimimos print(5, " ") y cambian valores...

'''2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores. '''
def divisores(n):
    return [i for i in range(1, n + 1) if n % i == 0]
print(divisores(12))
# return[ ] entre corchetes porque va a devolver una lista. El bucle for recorrerá range empezando por el 1 y terminando en 12+1, osea en 13 siempre y cuando el resto de 12 dividido entre i (entiendo que i es el resultado del propio bucle?) sea = 0, es decir se pueda dividir entre él mismo. 1ra vuelta -> 12 / 1 = 12 -> OK. 2a vuelta -> 12/2= 6 -> OK. 3a vuelta -> 12/3 = 4 ->OK. 4a vuelta -> 12/4 = 3 ->OK. 5a vuelta -> 12/5 = 2,4 -> NO OK, por tanto False, no cuenta. 6a vuelta-> 12/6= 2-> OK. 7a vuelta-> 12/7=1,71... ->NO OK(cndicion:False). 8a vuelta -> 12/8 = 1,5 (NO OK, False) ... 12a vuelta-> 12/12=1 (ok) y 13a vuelta->12/13=0,92... (False). Aquí termina el range, el último valido fue el nº12.

'''3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.'''
def nuevaLista(lista1):
    return list(set(lista1))
print(nuevaLista(['Carol', 'Laura', 'Pilar', 'Sergio', 'Laura', 'Pilar']))

# list() es una función que crea una lista. set() es una función que crea una colección de elementos sin orden concreto y sin duplicados. Sabiendo esto: devolvemos una lista que contiene los elementos que nosotros definamos en el argumento "lista1". Hemos definido esos elementos al final, cuando llamamos a la función. Set() se encarga de eliminar los duplicados.

'''4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.'''
def suma_digitos(n):
    return sum(int(digito) for digito in str(n))
print(suma_digitos(123))

# Defino una función que tomará el número 123. El resultado final que queremos es una suma, por tanto queremos que nos devuelva el resultado de lo que de la función sum(). Esta sum() tiene un bucle llamado digito que recorrerá el valor de n PERO transformado en string. No lo recorre y luego lo transforma en string, cuando lo recorre ya es string. Entonces: 1a vuelta ->resultado es "1", como ya tenemos el resultado de digito, se activa la función int() que en este caso coge el valor de digito y lo transforma en 1. De "1" a 1. 2a vuelta-> resultado de digito es "2" y resultado de int(digito) es 2. 3a vuelta-> resultado de digito es "3" y resultado de int(digito) es 3. No hay más vueltas porque no hay más números. Así pues sumamos los 3 resultados -> 1+2+3 = 6

# Duda: porque str() transforma "1" "2" "3" por separado y no "123", es por el bucle for?? -> lo pregunté en la clase y es porque está actuando sobre una lista. sum() es una funcion que va ligado a listas, por lo tanto aqui se asume que es una lista aunque no esté entre [] (creo que se refería a eso)

'''5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.'''
def contar_vocales(cadena):
    return sum(1 for letra in cadena if letra.lower() in 'aeiou')
print(contar_vocales('Hola Mundo'))
#(parecido al ejer 4?) el argumento cadena es "Hola Mundo". lower() devuelve texto en minúsculas. .lower() anexado a un objeto transforma en minúsculas sus letras/string.

#Dudas: Creo que lo que dice el bucle es: recorre la cadena si la cadena tiene alguna de las letras 'aeiou' y súmalas. Pero no entiendo por qué lower() no transforma todas las letras en minus. Ni entiendo el 1 delante del for, ni el "in" después del if.

'''6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista. '''
def elementos(list, n):
    return list[:n]
print(elementos([1,2,3,4,5,6],3))

# :n es un tipo de operacion de corte (slicing) que se aplica a secuencias -> invierte el orden de los elementos (consultar apuntes).
cadena = "hola"
cadena_invertida = cadena[::-1]
print(cadena_invertida)
#Dudas: cómo sería para sacar los 3 últimos? no me sale poniendo dos :: ni -3 (en el ejemplo "hola" de arriba sí sale)

''' 7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena. '''
def fcadena(cadena):
    mayusculas = sum(1 for letra in cadena if letra.isupper())
    minusculas = sum(1 for letra in cadena if letra.islower())
    return mayusculas, minusculas
print(fcadena("Me llamo Laura"))

# islower() function checkea y devuelve True si todos los caracteres son minúsculas. En el ejercicio, for recorre los elementos en cadena ("Me llamo Laura") y nos devuelve el resultdo si las letras son mayus/minus, pero además como está dentro de la función sum(), lo que nos devolverá es la suma de ese resultado, es decir la suma de los caracteres minus/mayus

# Duda: sigo sin entender el 1 delante del for