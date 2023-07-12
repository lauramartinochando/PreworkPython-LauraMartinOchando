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