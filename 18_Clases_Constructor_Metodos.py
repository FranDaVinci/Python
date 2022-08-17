from urllib.request import ProxyBasicAuthHandler


class coche():    #creamos un objeto a partir de una clase, la clase coche

    def __init__(self):   #iniciamos un constructor, con def init, los dos guiones delante de cada variable son para encapsularlas 
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
    
    def arrancar(self, arrancamos):  #creamos los métodos siempre con SELF dentro de los paréntesis, asi se diferencia de la funcion
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"

        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el cheque, no podemos arrancar"
        
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

            return True

        else:

            return False

miCoche=coche()

print(miCoche.arrancar(True))

miCoche.estado()


print("--------------------------A continuación creamos el segundo objeto--------------------------")

miCoche2=coche()

print(miCoche2.arrancar(False))

miCoche2.estado()