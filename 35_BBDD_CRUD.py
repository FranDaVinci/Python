import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confección'")#recordar que es CASE SENSITIVE

productos=miCursor.fetchall()
print(productos)

#codigo para actualizar un registro en la base de datos.
miConexion.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

#codigo para borrar un registro en la base de datos.
miConexion.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miConexion.commit()

miConexion.close()