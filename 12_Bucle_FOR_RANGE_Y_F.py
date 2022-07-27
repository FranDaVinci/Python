#con la F damos una notacion especial y con la i entre llaves, hacemos que el valor de la variable se concatene con el texto.
#sin la F python no entiende la concatenacion, de ahí la notación especial.
for i in range(5):
    print(f"Valor de la variable {i}")

#los tres valores en RANGE, son por donde empezará, hasta donde tiene que llegar y los saltos que debe dar que son de 4 en 4.
for i in range(5, 50, 4):
    print(f"valor de la variable {i}")


#En esta caso validaremos un email a través del bucle FOR con el método LEN, que contará la longitud del email introducido
#y dará una vuelta de bucle por cada letra hasta que encuentre la @
valido=False

email=input("itroduce tu email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("Email correcto")
else:
    print("Email no valido")
