#Las tuplas son igual que las listas pero son inmutables, no permiten añadir, eliminar o mover elementos.
#no append, no extend, no remove.
#Pêrmiten el metodo index de la misma manera que en las listas.
#si permiten comprobar si un elemento se encuentra en la tupla.
#a diferencia de las listas, los elementos se encierran entre paréntesis aunque no son obligatorios, si recomendables.

tupla1 = ("Alba", 2, "Francisco", 12, "Sonic", 12, 12)
print (tupla1)
print (tupla1[2])#aqui le indicamos la posicion que queremos que nos muestre.

#Convertir una tupla a lista y viceversa

lista1 = list(tupla1)
print (lista1) #aquí la convertimos en lista con LIST

tupla1 = tuple(lista1)
print (tupla1) #aquí la convertimos en tupla con TUPLE

#con la función IN conseguimos el mismo resultado que en las listas, comprobar si un elemento está dentro de la tupla.
print ("Alba" in tupla1)
print ("Pepe" in tupla1)

#con el método COUNT nos devuelve el número de veces que se repite un elemento dentro de una tupla.
print (tupla1.count (12))
print (tupla1.count ("Alba"))

#con el método LEN nos devolverá la longitud de la tupla
print (len(tupla1))

#Tuplas unitarias, o que solo contendrán un elemento, tienes que poner una coma "," justo despues del primer elemento
tupla2 = ("Juan",)
print (len(tupla2))

#empaquetado y desempaquetado de tuplas
tupla3 =("Fran", 12, 6, 1984)
nombre, dia, mes, anio = tupla3
print (nombre)
print (dia)
print (mes)
print (anio)
