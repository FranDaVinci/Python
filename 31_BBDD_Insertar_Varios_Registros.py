import sqlite3

miConexion=sqlite3.connect("PrimeraBase") 
 
miCursor=miConexion.cursor() #creacion del puntero o cursor

#A CONTINUACION CODIGO PARA LA CREACION DE UNA TABLA SQL

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#PARA LA PROXIMA LINEA DE EJECUCION HAY QUE COMENTAR LA LINEA DE ARRIBA, PARA PODER INSERTAR DATOS.

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN', 15, 'DEPORTES')")#insercion de datos en la bbdd

variosProductos=[#creamos una tupla con todos los registros que quieras insertar de golpe
    ("camiseta", 10, "deportes"),
    ("jarrón", 90, "ceramica"),
    ("camión", 20, "jugueteria")
]
#utilizamos executemany como instruccion para insertar varios registros a la vez
miConexion.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)#ponemos un simbolo de interrogacion por cada valor insertado.

#para ver la informacion que le pidamos haremos los siguiente
miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()#la instruccion fetchall nos devuelve una lista con toda la informacion que le pidamos
print(variosProductos)#lo imprimimos para ver los productos

for producto in variosProductos:
    print(producto)# aqui nos imprime en un bucle y de forma ordenada los productos dentro de la base de datos

for producto in variosProductos:
    print("Nombre Articulo: ", producto[0], " Sección: ", producto[2])# aqui nos lo mostraria de forma mas precisa


miConexion.commit()#codigo para insertar los datos en la bbdd





miConexion.close()