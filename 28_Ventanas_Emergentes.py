from tkinter import *
#hay que importar la libreria especifica para las ventanas emergentes, MESSAGEBOX
from tkinter import messagebox 

root=Tk()

#creamos una funcion para agregar un mensaje emergente a la opcion "acerca de...", con MESSAGEBOX.SHOWINFO
def infoAdicional():
    messagebox.showinfo("Fran Ramirez", "El mejor artista del mundo")#Showinfo muestra la informacion

def avisoLicencia():#SHOWWARNING es igual que showinfo, solo cambia el icono
    messagebox.showwarning("AVISO", "La licencia ha expirado Gilipoyas")

def salirAplicacion():
    #con ASKQUESTION la ventana emergente te hace una pregunta
    #valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")
    #con ASKOKCANCEL la ventar emergente te dará las opciones ok o cancel
    if valor==True:
        root.destroy()#con .destroy saldrás al aceptar la pregunta

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "Documento bloqueado, reintentar o cancelar")
    if valor==False:
        root.destroy()

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
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)


archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)#llamamos a la funcion con command=
archivoAyuda.add_command(label="Ayuda")

#con add_cascade añadimos el nombre que llevará visible cada seccion
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()