import pickle #volvemos a importar la biblioteca PICKLE

fichero=open("lista_nombres", "rb") #RB significa read binary

lista=pickle.load(fichero) #con LOAD cargamos los datos

print(lista) #se nos imprimirá la lista que habiamos codificado en el ejercicio anterior.