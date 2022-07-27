#Los Diccionarios

#Son unas estructuras de datos que nos permite almacenar valores de diferente tipo (enteros, cadenad de texto, decimales)
#e incluso listas y otro diccionarios.

#La principal caracteristica de los diccionarios es que los datos se almacenan asociados a una clave de tal forma
#que se crea una asociacion de tipo CLAVE:VALOR para cada elemento  almacenado.

#Los elementos almacenados no estan ordenados. El orde es indiferente a la hora del almacenar información en un diccionario.

midiccionario = {"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid","Reino Unido":"Londres"}
print(midiccionario["Francia"])
print(midiccionario["España"])
print(midiccionario)

midiccionario ["Italia"]="Lisboa"  #añadimos un elemento al diccionario y cometemos un error a conciencia
print(midiccionario)
midiccionario ["Italia"]="Roma" #lo arreglamos sobreescribiendo
print(midiccionario)

del midiccionario ["Reino Unido"] # DEL para borrar un elemento del diccionario
print(midiccionario)

diccionario2 = {23:"Jordan", "Mosquetero":3} #distintos valores
print (diccionario2)

#creamos una tupla para almacenarla en un diccionario
mitupla = ("España", "Francia", "Alemania")
diccionario3 = {mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Berlin"} 
print (diccionario3) 
print (diccionario3["España"])

#una tupla dentro de un elemento de un diccionario
diccionario4 = {"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid", 23:"Jordan", "anillos":[1991,1992,1993,1997,1998]}
print(diccionario4["anillos"])

 #un diccionario dentro de un diccionario
diccionario4 = {"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid", 23:"Jordan", "anillos":{"temporadas":[1991,1992,1993,1997,1998]}}
print(diccionario4["anillos"])
print(diccionario4)
print(diccionario4.keys())#imprime las claves que pertenecen al diccionario
print(diccionario4.values())#imprime los valores del diccionario
print(len(diccionario4))#imprime la longitud del diccionario



