from tkinter import *
from tkinter import filedialog #para una ventana de abri archivo hay que importar la libreria FILEDIALOG

root=Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="")
    print(fichero)
#filedialog.askopenfilename crea una ventana emergente de busqueda.
#initialdir= hace que se abra la busqueda donde tu le digas
#filetypes= creas una tupla con el nombre y las extensiones que quieres que visualice al hacer la busqueda.

Button(root, text="Abrir fichero", command=abreFichero).pack()



root.mainloop()