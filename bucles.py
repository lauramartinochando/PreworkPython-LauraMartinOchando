'''
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
'''
#1
numeros = [1,2,3,4,5,6,7,8,9,10]
for ejercicio in numeros:
    print(ejercicio)
#2
y = 1
while y <= 20:
    if y %2 == 0:
        print(y)
    y += 1
#3
suma = 0
for ejercicio3 in range(101):
    suma += ejercicio3
print(suma)