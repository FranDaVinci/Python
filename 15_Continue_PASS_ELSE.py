#instrucciones CONTINUE, PASS y ELSE. (PASS se usa en muy muy pocas ocasiones, y se utiliza para dejar un trabajo a medias para continuar mas tarde, hace que el programa pase de esa parte del codigo)

from operator import truediv


for letra in "python":
    if letra == "h":
        continue 
    print("Viendo la letra " + letra)

##############################################

nombre = "Fran Ramirez"
contador = 0

for i in nombre:
    if i==" ":
        continue #aqui continue hace que se ignoren los espacios en blanco entre palabras, para dar la longitud exacta.
    contador=contador+1

print(contador)    
print(len(nombre))

###############################################

email=input("introduzca su e-mail: ")

for i in email:
    if i=="@":
        arroba=True
        break;

else:
    arroba=False

print(arroba)