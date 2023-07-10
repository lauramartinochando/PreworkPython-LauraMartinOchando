'''
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos
'''

#1
x = 4
if x > 0:
  print("Es un número positivo")
else:
  print("Es un número negativo")
#2
x = 15
if x % 2 == 0:
  print("Es un número par")
else:
  print("Es un número impar")
#3
x = 22
y = 101
s = -7
num_mayor = max(x,y,s)
print(num_mayor)
