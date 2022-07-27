# Operador IN sin lower
print("Asignaturas optativas año 2022")
print("Optativas: Informatica Grafica - Pruebas de Software - Usabilidad y Accesibilidad")
asignatura=input("Escribe la asignatura escogida: ")

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)

else:
    print("La asignatura escogida no está contemplada")


#recordad que Python es case sensitive, que no distingue entre mayusculas y minusculas, habria que escribir siempre de la 
#misma forma que lo escribiste en el programa

print("Asignaturas optativas año 2022")
print("Optativas: Informatica Grafica - Pruebas de Software - Usabilidad y Accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()#con LOWER nos aseguramos que nadie escribirá con mayusculas, llevando nuestro programa a error

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)

else:
    print("La asignatura escogida no está contemplada")