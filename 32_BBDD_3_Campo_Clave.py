import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

#execute se usa siempre para ejecutar una orden de codigo SQL
miCursor.execute(''' 
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PERCIO INTEGER, 
    SECCION VARCHAR(20))
''')
#crear una tupla para los productos
productos=[
    ("AR01", "pelota", 20, "juguetería"),
    ("AR02", "pantalon", 15, "confeción"),
    ("AR03", "destornillador", 25, "ferretería"),
    ("AR04", "jarrón", 45, "cerámica"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

miConexion.commit()

miConexion.close()