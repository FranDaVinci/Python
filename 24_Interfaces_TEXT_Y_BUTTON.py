#Text sirve para introducir un cuadro de texto largo
#Button, Son botones para interactuar con la interfaz

from tkinter import *  #importamos todo de la libreria TKINTER

raiz=Tk()   #inicializamos el constructor
raiz.title("Ventana de prueba para interfaz gráfica")

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack() #empaquetamos el frame

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="left") #aqui configuramos algunos estilos

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10,  pady=10)
cuadroPass.config(show="*") #aqui ocultamos la contraseña tambien con .config

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10,  pady=10)
cuadroApellido.config(fg="blue", bg="yellow")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10,  pady=10)

cuadroComentario=Text(miFrame, width=16, height=5)#Esto es una caja de comentarios y hemos dado medidas
cuadroComentario.grid(row=4, column=1, padx=10,  pady=10)

scrollVert=Scrollbar(miFrame, command=cuadroComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")#con nsew se adapta a la caja de comentario
#añadimos manualmente una barra de scroll a la caja de comentarios , con command y YVIEW para que sea vertical.

cuadroComentario.config(yscrollcommand=scrollVert.set)#aqui para que el posicionamiento del scroll este bien siempre.

nombreLable=Label(miFrame, text="Nombre: ")#con Label vamos creando los cuadros de texto
nombreLable.grid(row=0, column=0, sticky="w", padx=10, pady=10)

passLable=Label(miFrame, text="Contraseña: ")
passLable.grid(row=1, column=0, sticky="w", padx=10, pady=10)

apellidoLable=Label(miFrame, text="Apellido: ")
apellidoLable.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLable=Label(miFrame, text="Dirección: ")
direccionLable.grid(row=3, column=0, sticky="w", padx=10, pady=10)

comentarioLable=Label(miFrame, text="Comentario: ")
comentarioLable.grid(row=4, column=0, sticky="w", padx=10, pady=10)

def codigoBoton():

    minombre.set("Fran")#con esta variable que definimos arriba del todo estamos diciendo que al pulsar el boton 
    #enviar, se escriba el nombre FRAN en el cuadro nombre

BotonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
#Asi creamos el boton y con COMMAND podemos asignarle una funcion para que tenga funcionalidades.
BotonEnvio.pack()

raiz.mainloop() #Siempre acabamos una interfaz con la raiz y la funcion .MAINLOOP()