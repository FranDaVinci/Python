#Ejercicio 1 Video 11
#Crea un programa que pida dos numeros por teclado y devuelva el mayor de los dos. 

num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))

def DevuelveMax(n1, n2):
    if n1<n2:
       print(n2)
    elif n2<n1:
       print(n1)
    else:
        print("son iguales")

print ("El numero mayor es: ")

DevuelveMax(num1, num2)
        
        