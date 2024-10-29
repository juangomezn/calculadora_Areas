from Modulos.modulos import *
from time import sleep

while True:
    menu()

    opc = input("\nIngrese la opcion de la figura que desea calcular el area\n")

    if opc not in ["0", "1", "2", "3", "4", "5"]:
        print("Opcion invalida")
        print("Ingrese una de las opciones mostradas en el menu")
        continue

    if opc == "1":
        area_Rectangulo()

    if opc == "2":
        area_Circulo()

    if opc == "3":
        area_Triangulo()

    if opc == "4":
        area_Rombo()

    if opc == "0":
        print("Gracias por utilizar el programa de calculo de areas")
        print("Saliendo del programa...")
        sleep(1)
        break