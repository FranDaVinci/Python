#Ejercicio 2 del video 11 de pildoras informaticas
#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
#deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
#personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por
#teclado).

nombre=input("Introduzca su nombre: ")
direccion=input("Introduzca su dirección: ")
telf=input("Introduzca su telefono: ")

datos=[nombre, direccion, telf]

print("los datos personales son: " + datos[0] + " " + datos[1] + " " + datos[2])