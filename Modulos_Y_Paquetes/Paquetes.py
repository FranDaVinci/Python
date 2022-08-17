'''
PAQUETES
Los paquetes son directorios donde se almacenarán modulos relacionados entre sí.
Sirven para organizar y reutilizar los módulos.
Y se crean: creando una carpeta con un archivo __init__.py
En el interior de esa carpeta se meteran todos los módulos 

'''
def sumar(op1, op2):
    print ("El resultado de la suma es: ", op1+op2)

def restar(op1, op2):
    print ("El resultado de la resta es: ", op1-op2)

def multiplicar(op1, op2):
    print ("El resultado de la multiplicación es: ", op1*op2)

def dividir(dividendo, divisor):
    print ("El resultado de la división es: ", dividendo/divisor)

def potencia(base, exponente):
    print ("El resultado de la suma es: ", base**exponente)

def redondear(numero):
    print ("El resultado del redondeo es: ", round(numero)) #ROUND redondea hacia arriba o hacia abajo un numero decimal
