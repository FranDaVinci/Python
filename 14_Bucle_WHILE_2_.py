import math
from socket import inet_ntoa

#Programa para hallar la raiz cuadrada de un numero con un numero contado de veces

print ("Programa de calculo de raíz cuadrada")
numero=int(input("Introduce un número por favor:"))

intentos=0

while numero<0:
    print("no se puede hallar la raíz cuadrada de un número negativo")

    if intentos==2:
        print("Has consumido tus intentos. El programa ha finalizado")
        break;

    numero=int(input("Introduce un número por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)#math es un metodo que hay que importarlo en las primeras lineas de código
    print("la raíz cuadrada de " + str(numero) + " es " + str(solucion))