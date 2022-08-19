from tkinter import *  #importamos todo de la libreria TKINTER

raiz=Tk()   #inicializamos el constructor
raiz.title("Ventana de prueba para interfaz gráfica")

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack() #empaquetamos el frame

cuadroNombre=Entry(miFrame)
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

nombreLable=Label(miFrame, text="Nombre: ")#con Label vamos creando los cuadros de texto
nombreLable.grid(row=0, column=0, sticky="w", padx=10, pady=10)

passLable=Label(miFrame, text="Contraseña: ")
passLable.grid(row=1, column=0, sticky="w", padx=10, pady=10)

apellidoLable=Label(miFrame, text="Apellido: ")
apellidoLable.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLable=Label(miFrame, text="Dirección: ")
direccionLable.grid(row=3, column=0, sticky="w", padx=10, pady=10)

raiz.mainloop() #Siempre acabamos una interfaz con la raiz y la funcion .MAINLOOP()