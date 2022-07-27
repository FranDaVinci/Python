#concatenacion de operadores de comparacion

salario_presidente = int(input("Introduce salario de presidente: "))
print("Salario Presidente: " + str(salario_presidente))

salario_director = int(input("Introduce salario de director: "))
print("Salario Director: " + str(salario_director))

salario_jefe = int(input("Introduce salario de jefe: "))
print("Salario Jefe: " + str(salario_jefe))

salario_peon = int(input("Introduce salario de peon: "))
print("Salario Peón: " + str(salario_peon))

if salario_peon<salario_jefe<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo está fallando")