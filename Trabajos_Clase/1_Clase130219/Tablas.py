#!/usr/bin/env python3
#García Espinosa David Alexis
#Programa para imprimir tablas de verdad
from tabulate import tabulate #Mandamos a llamar una librería para hacer tablas
A=[True,False]
B=[True,False]
print("Programa para conocer tablas de los operadores AND, OR, NOT")
print("Seleccione una tabla 1,2,3  respectivamente")
val =  int(input("¿Cual tabla deseas?"))
tab = [['V','V'],['F','V'],['V','F'],['F','F']]
tab2 = ['V','F']
if val == 1:
 print(tabulate(tab)) #Función para hacer tablas bajo un arreglo dado
 for i in range(2):   #Iteración de i en los 2 valores V y F
  for j in range(2):  #Iteración de j para obtener todas los combinaciones de la tabla
   print(A[i] and B[j]) #Evaluación e impresión de los resultados dentro de la tabla
else:
 if val == 2:		#Se evalua e itera del mismo caso que en el anterior
  print(tabulate(tab))
  for k in range(2):
   for h in range(2):
     print(A[k] or B[h])
 else:
   if val == 3:
    print(tabulate(tab2))
    for s in range(2):
       print(not A[s])
   else:
    print("No has escogido una de las tablas favor de ingresar [1,2 o 3]")
