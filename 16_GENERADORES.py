#Generadores
#Son estructuras que extraen valores de una funcion y se almacena en objetos iterables(Que se pueden recorrer)
#Estos valores se almacenan de uno en uno
#Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita el siguiente.
#Esta caracteristica, es conocida como "suspension de estado".

#Que utilidad tienen:
#son mas eficientes que las funciones tradicionales
#muy utiles con listas de valores infinitos
#bajo determinados escenarios, sera muy util que un generador devuelva los valores de uno en uno


#Creamos una funcion tradicional y comparamos
"""
def generaPares(limite):
    
    num=1
    milista=[]

    while num<limite:
        milista.append(num*2)
        num=num+1

    return milista

print(generaPares(10)) 

"""

#A partir de aqui hacemos lo mismo pero con un generador

def generaPares1(limite1):

    num1=1

    while num1<limite1:

        yield num1*2 #usamos YIELD en vez de return
        num1=num1+1

devuelvePares=generaPares1(10)

print(next(devuelvePares)) # Y para que vaya de uno en uno en cada llamada de la funcion usamos NEXT dentro de PRINT

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))
