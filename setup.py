from setuptools import setup

setup (
    name="paquetecalculo",
    version=1.0,
    description="paquete de calculos",
    author="Fran",
    author_email="fran.ramire.art@gmail.com",
    url="fran.com",
    packages=["Modulos_Y_Paquetes","Paquetes.py"]
)

#y despues en la consola de Python o la de windows, pondremos esto para crear el paquete distribuible.

#PS C:\Users\Fran Ramírez\Desktop\Python> python setup.py sdist

#para instalarlo en cualquier parte seguiremos el siguiente paso, tambien en consola.

#PS C:\Users\Fran Ramírez\Desktop\Python\dist>pip3 install "nombre_del_paquete"

'''
con esto conseguiremos crear un paquete distribuible para poderlo mandar a cualquier parte
e instalarlo en otros equipos
'''