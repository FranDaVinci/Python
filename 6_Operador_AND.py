#utilizando los operador AND 

print("Programas de becas 2022")

distancia = int(input("Introduce la distacia en KM de tu casa a la escuela: "))
print(distancia)

hermanos = int(input("Introduce el nº de hermanos que tienes: "))
print(hermanos)

salario = int(input("Introduce el salario anual de tu familia: "))
print(salario)

if distancia>40 and hermanos>2 and salario<=20000:
    print("Enhorabuena, puedes optar a una plaza para la beca")

else:
    print("Lo sentimos, no puedes optar a la beca")