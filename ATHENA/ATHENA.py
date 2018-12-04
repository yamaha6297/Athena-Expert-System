from expertSystem import clientType
from methods import checkInt
import os

client = 0
bandera = True

while bandera:
    os.system('clear')
    print("****** ATHENA Expert System ******\n")
    name = input("Ingrese su nombre: ")
    if name.isalpha():
        bandera = False
    
while client < 1 or client > 3 or type(client) != int:

    os.system('clear')
    print("****** ATHENA Expert System ******\n")
    print("Bienvenido " + name.upper() + ", que celular deseas adquirir?: \n")
    print("1- Un modelo especifico")
    print("2- Un celular con caracteristicas definidas")
    print("3- No estoy seguro de lo que busco\n")
    client = checkInt("Elija opcion: ")

clientType(client)
