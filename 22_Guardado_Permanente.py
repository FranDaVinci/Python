import pickle #aqui necesitamos tambien importar la biblioteca pickle

class persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad

        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
class listapersonas:
    personas=[]

    def __init__(self):
        listadepersonas=open("ficheroexterno","ab+") #ab significa agregar informacion binaria
        listadepersonas.seek(0)

        try:
            self.personas=pickle.load(listadepersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        
        except:
            print ("El fichero está vacío")
        
        finally:
            listadepersonas.close()
            del(listadepersonas)

    def agregarpersonas(self, p):
        self.personas.append(p)
        self.guardarpersonasenficheroexterno()
    
    def mostrarpersonas(self):
        for p in self.personas:
            print(p)

    def guardarpersonasenficheroexterno(self):
        listadepersonas=open("ficheroexterno", "wb")
        pickle.dump(self.personas, listadepersonas)
        listadepersonas.close()
        del(listadepersonas)

    def mostrainfoficheroexterno(self):
        print("La informacion del fichero externo es la siguiente")
        for p in self.personas:
            print(p)

milista=listapersonas()

person=persona("Sandra", "Femenino", 29)
milista.agregarpersonas(person)
person=persona("Antonio", "Masculino", 39)
milista.agregarpersonas(person)
person=persona("Maria", "Femenino", 26)
milista.agregarpersonas(person)
milista.mostrainfoficheroexterno()

# milista.mostrarpersonas()