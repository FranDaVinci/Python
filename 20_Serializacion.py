import pickle #importamos la biblioteca PICKLE

lista_nombres=["pedro", "ana", "maria", "isabel"]

#creamos un fichero externo

fichero_binario=open("lista_nombres", "wb") #WB es escritura binaria

pickle.dump(lista_nombres, fichero_binario) #con DUMP hacemos el volcado de datos

fichero_binario.close() #cerramos el fichero

del (fichero_binario)

#al ejecutar este programa se nos creara el archivo lista_nombre, codifcada en codigo binario.