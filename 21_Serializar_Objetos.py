import pickle #importamos la biblioteca PICKLE

#Serializacion de objetos, primero creamos el objeto
class vehiculo():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print ("Marca: ",self.marca,"\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

coche1=vehiculo("Mazda", "MX5") #creamos varios objetos a partir de la clase vehiculo
coche2=vehiculo("Seat", "Leon")
coche3=vehiculo("Renault", "Zafira")

coches=[coche1, coche2, coche3]

fichero=open("LosCoches","wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)


