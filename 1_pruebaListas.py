#las listas son como los arrays y empiezan igualmente en la posicion 0, van entre corchetes.

lista1 = ["Fran", "Sandra", 12, 2108, "Alba"]
print(lista1[1])

lista1.extend (["Blanca", 2012, "Aurora", "Pepe"]) #con extend podemos añadir mas elementos a la lista.
print(lista1)

lista1.append ("Raul") #con append añadimos un elemento al final de la lista.
print(lista1)

lista1.insert (3, "Jesus") #con insert insertamos un elemento en la posición concreta que le indiquemos antes.
print (lista1)

print (lista1.index("Aurora")) #con index nos devolverá el indice o posición de un elemento.

print ("Alba" in lista1) #la función in nos devolverá true o false dependiendo si ese elemento se encuentra en la lista.

lista1.remove (2108) #con la funcion remove eliminamos el elemento que le indiquemos.
print (lista1)

lista1.pop () #con la funcion POP() eliminamos el elemento último de la lista.
print (lista1)

#Sumar listas

lista2 =  [89, "Francesca", "Robert"]
lista3 = lista1 + lista2   #Con el operador + sumamos listas, como si se concatenaran.
print (lista3)

lista4 = [45, 34, 3, 6, 7, 94] * 3  #con el operador * nos mostrará la lista el numero de veces que hayamos puesto.,
print(lista4) 