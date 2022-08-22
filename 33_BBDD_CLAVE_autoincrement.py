import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

#execute se usa siempre para ejecutar una orden de codigo SQL
#AUTOINCREMENT para una clave autoincrementable
miCursor.execute(''' 
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PERCIO INTEGER, 
    SECCION VARCHAR(20))
''')
#crear una tupla para los productos
productos=[
    ("pelota", 20, "juguetería"),
    ("pantalon", 15, "confeción"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica"),
]
#introducimos NULL en el campo de la clave autoincrementable
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()