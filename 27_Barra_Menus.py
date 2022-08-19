from tkinter import *

root=Tk()

root.title("Ventana de Prueba")

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#creamos una variable para cada seccion del menú, le decimos que es igual Menu que esta dentro de barraMenu
#con ADD_COMMAND añadiremos los subelementos que queramos dentro de Archivo, igual para Herramientas y demas.
archivoMenu=Menu(barraMenu, tearoff=0)#con TEAROFF=0 quitamos la barra separadora por defecto
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()#crea una linea para separar grupos dentro del menu
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)


archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")
archivoAyuda.add_command(label="Ayuda")

#con add_cascade añadimos el nombre que llevará visible cada seccion
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()