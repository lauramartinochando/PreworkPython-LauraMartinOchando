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
#return[ ] entre corchetes porque va a devolver una lista. El bucle for recorrerá range empezando por el 1 y terminando en 12+1, osea en 13 siempre y cuando el resto de 12 dividido entre i (entiendo que i es el resultado del propio bucle?) sea = 0, es decir se pueda dividir entre él mismo. 1ra vuelta -> 12 / 1 = 12 -> OK. 2a vuelta -> 12/2= 6 -> OK. 3a vuelta -> 12/3 = 4 ->OK. 4a vuelta -> 12/4 = 3 ->OK. 5a vuelta -> 12/5 = 2,4 -> NO OK, por tanto False, no cuenta. 6a vuelta-> 12/6= 2-> OK. 7a vuelta-> 12/7=1,71... ->NO OK(cndicion:False). 8a vuelta -> 12/8 = 1,5 (NO OK, False) ... 12a vuelta-> 12/12=1 (ok) y 13a vuelta->12/13=0,92... (False). Aquí termina el range, el último valido fue el nº12.