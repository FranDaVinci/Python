#Utilizando la instruccion YIELD FROM

def devuelveCiudad(*ciudades): #el asterisco quiere decir que recibira un numero indeterminado de elementos.
    for elemento in ciudades:
        #for subelemento in elemento: "aqui sin el from con un for anidado"
            yield from elemento

ciudadesDevueltas=devuelveCiudad("Madrid", "Barcelona", "Bilbao", "Sevilla")

print(next(ciudadesDevueltas)) #nos devolvera los tres primeros elementos del subelemento
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))



