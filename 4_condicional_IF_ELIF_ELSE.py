#if debe ir seguido de un else, a noser que haya varios if, entonces lo conveniente seria poner un if y despues elif hasta el #ultimo que seria un else

print ("Verificacion de acceso a la universidad")

nota = int(input("introduce tu nota por favor: "))

if nota < 5:
    print("Insuficiente")

elif nota < 6:
    print("Suficiente")

elif nota < 7:
    print("Bien")

elif nota < 9:
    print("Notable")

else:
    print("Sobresaliente")
