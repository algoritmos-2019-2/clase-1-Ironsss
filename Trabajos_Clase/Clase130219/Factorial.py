#!/usr/bin/env python3

#García Espinosa David Alexis Algoritmos C. 2019-2
#Programa para Imprimir el factorial de un número

num = int(input("¿Cuál es tu número?"))
fac = 1
if num<=0 : 
 print("Factorial no definido para numeros negativos y 0!=1")

else:

 while(num !=0):
    fac= fac*num  #El primer ciclo inicia con 1 por el numero dado 
    num = num-1   #continuando por igualar  fac por el producto hasta que num = 0
 print(fac)
 print("Hasta aqui llega tu cuenta")
