#!/usr/bin/env python3

#García Espinosa David Alexis Algoritmos C. 2019-2
#Programa para Imprimir la secuencia hasta cierto digito en la sucesión

num = int(input("¿cuantos terminos de la sucesión deseas?"))
x = 0
y = 1
for i in range(num):
    print(x)
    x,y= y,x+y	#Definición en paralelo del algortimo no entendido al 100%(asignación en paralelo)
