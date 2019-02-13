#!/usr/bin/env python3
#García Espinosa David Alexis Algoritmos C. 2019-2 
#Programa que te suma los numeros anteriores a uno dado  

sum = 0
num = int(input("¿Cual es tu numero?"))

for i in range(num+1):
 sum = sum + i
print("La suma de tus numeros hasta")
print(num)
print("es:")
print(sum)

