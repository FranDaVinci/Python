#libreria necesaria para establecer la conexion con mysql
import mysql.connector

miConexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "ponermicontraseña", 
    db = "nombredelabasededatos"   
)#host, usuario, contraseña y nombre de la base de datos, obligatorio para establecer la conexion.

if miConexion.is_connected(): #conprobamos que la conexion se establece correctamente
    print("conexion establecida correctamente")

miCursor = miConexion.cursor()

miCursor.execute("INSERT INTO pinturas VALUES (NULL, '200X150', 'OLEO', 'LIENZO', 2022)")

miConexion.commit()#con commit enviamos las peticiones a la base de datos


miConexion.close()

if not miConexion.is_connected(): #comprobamos que se cierra la conexion con la base de datos
    print("Conexión cerrada satisfactoriamente")
