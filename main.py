from Modulos.modulos import *

while True:
    menu()

    opc = input("Ingrese la opcion de la figura que desea calcular el area \n")

    if opc == "1":
        area_Rectangulo()

    if opc == "2":
        area_Circulo()

    if opc == "3":
        area_Triangulo()

    if opc == "4":
        area_Rombo()