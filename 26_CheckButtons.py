from tkinter import *

root=Tk()
root.title("Ejemplo")

#creamos variables de tipo entero para asignarlas a cada checkbutton, para que al estar seleccionada nos devuelva 1
#y sino nos devuelve 0
playa=IntVar()
montana=IntVar()
piscina=IntVar()

def OpcionesViaje():
    opcionEscogida=""

    if(playa.get()==1):#GET para que muestre lo escogido
        opcionEscogida=opcionEscogida+" playa"
    
    if(montana.get()==1):
        opcionEscogida=opcionEscogida+" montaña"
    
    if(piscina.get()==1):
        opcionEscogida=opcionEscogida+" piscina"

    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="avion.png")#creamos una variable y con PHOTOIMAGE introducimos una imagen y en FILE le decimos la ruta.
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destino:", width=50).pack()

#Con ONVALUE le diremos que el checkbutton está seleccionado
#con OFFVALUE le diremos que el checkbutton no está seleccionado
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=OpcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=OpcionesViaje).pack()
Checkbutton(frame, text="Piscina", variable=piscina, onvalue=1, offvalue=0, command=OpcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()