'''
Pasos a seguir para conectar con Bases de datos:

1- Abrir-Crear conexión.
2- Crear puntero o cursor.
3- Ejecutar query (Consulta)SQL.
4- Manejar los reusultados de la query(consulta)
   -Insertar, leer, actualizar, borrar(CREATE, READ, UPDATE, DELETE)
5- Cerrar puntero.
6- Cerrar conexión.

'''

#en esta primera vez escribiremos codigo para SQLITE

import sqlite3

miConexion=sqlite3.connect("PrimeraBase") 
 
miCursor=miConexion.cursor() #creacion del puntero o cursor

#A CONTINUACION CODIGO PARA LA CREACION DE UNA TABLA SQL

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#PARA LA PROXIMA LINEA DE EJECUCION HAY QUE COMENTAR LA LINEA DE ARRIBA, PARA PODER INSERTAR DATOS.

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN', 15, 'DEPORTES')")#insercion de datos en la bbdd

miConexion.commit()#condigo para insertar los datos en la bbdd





miConexion.close()