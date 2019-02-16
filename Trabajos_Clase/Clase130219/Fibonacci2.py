#!/usr/bin/env python3

#García Espinosa David Alexis Algoritmos C. 2019-2
#Programa para Imprimir el factorial de un número al definir una función y hacerla recursiva obtener los valores deseados 

num = int(input("¿Cuantos terminos de la sucesión deseas?"))
x=0
y=1
for i in range(num):
     print(x)
     t=y   #se va haciendo una asignación iterada 
     y=x+y #Es conocida como la forma más tradicional para definir la sucesión
     x=t   #Tomando los valores de f(n-1) + f(n-2)
     
