#ejemplo con bucle FOR 

contador = 0
miEmail = input("Introduce tu dirección de Email:")

for i in miEmail:

    if (i=="@" or i=="."):
        contador=contador+1
    
if contador==2: #or contador >= 2:  aquí se podria modificar para hacerlo mas efectivo
    print("Email correcto")
else:
    print("Email incorrecto")


#######################################################################################


for i in range(3):
    print("Jelou") #con RANGE se repetira el bucle las veces que pongas entre parentesis.

