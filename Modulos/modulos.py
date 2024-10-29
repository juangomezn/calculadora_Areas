def menu():
    print("     Calculadora de Areas    ")
    print("""   
                1. Area de un rectangulo
                2. Area de un circulo
                3. Area de un triangulo
                4. Area de un rombo
                0. Salir""")
    
def area_Rectangulo():
    print("Ingrese la medida del largo: ")
    Lado_1 = int(input())
    print("Ingrese la medida del ancho: ")
    Lado_2 = int(input())
    calculo = Lado_1 * Lado_2
    print(f"El area de tu rectangulo es, {calculo}")

def area_Circulo():
    print("Ingrese la medida del radio del circulo")
    Lado_1 = int(input())
    calculo = Lado_1**2
    calculo = calculo * 3.14
    print(f"El resultado del area es, {calculo}")

def area_Triangulo():
    print("Ingrese la medida de la base del triangulo")
    Lado_1 = int(input())
    print("Ingrese la medida de la altura del triangulo")
    Lado_2 = int(input())
    calculo = (Lado_1*Lado_2)/2
    print(f"El area del triangulo es, {calculo}")