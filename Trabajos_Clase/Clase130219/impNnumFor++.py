#!/usr/bin/env python3
#García Espinosa David Alexis Algoritmos C. 2019-2 
#Programa  Para imprimir  los números del 0 al N dado e imprimir dichos números

sum = 0
s = 0
num = int(input("¿Cual es tu numero?"))

for i in range(num+1):
 print(i)
 sum = sum + i
print("La suma de tus numeros hasta")
print(num)
print("es:")
print(sum)

