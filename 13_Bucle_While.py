#Ejemplos con bucle WHILE

from turtle import st


i=1

while i<=10:
    print("Ejecucion " + str(i))
    i=i+1

print("terminó la ejecución")

#Ejemplo para preguntar la edad correcta

edad=int(input("introduzca su edad: "))

while edad < 0 or edad > 120:
    print("has itroducido una edad incorrecta, vuelve a intentarlo")
    edad=int(input("introduzca su edad: "))#si escribe una edad negativa vuelve a ejecutar el bucle while todas las veces hasta que introduzcas una fecha correcta

print("Gracias por introducir su edad correcta")
print("Edad del aspirante " + str(edad))