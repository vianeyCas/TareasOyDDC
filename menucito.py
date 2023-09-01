#Tarea 993 Menucito de Mariana Castro
def opcion1():
    print("Esta es la opcion 1.")
    decimal = int(input("¿Que numero convertiras a binario?: "))  
    binario = ""
    cociente = decimal

    while cociente != 0:  
        residuo = cociente % 2
        cociente = cociente // 2
        binario = str(residuo) + binario 

    print("Binario:", binario)

def opcion2():
    print("Esta es la opcion dos.")
    binario = input("Ingresa un binario para convertirlo a decimal: ")
    decimal = 0
    base = 1

    for bit in binario[::-1]:
        if bit == '1':
            decimal += base
        base *= 2

    print("Decimal:", decimal)

def opcion3():
    print("Esta el la opcion 3.")
    uno = int(input("Ingrese un numero ")) 
    dos = int(input("Ingrese el otro numero: "))  
    suma = uno + dos
    print("Suma:", suma)

    resta = uno - dos
    print("Resta:", resta)

    multiplicacion = uno * dos
    print("Multiplicación:", multiplicacion)

    division = uno / dos
    print("División:", division)

    resto = uno % dos
    print("Resto:", resto)

while True:
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    
    opcion = input("Selecciona")
    
    if opcion == "1":
        opcion1()
    elif opcion == "2":
        opcion2()
    elif opcion == "3":
        opcion3()
    elif opcion == "4":
        print("Salir.")
        break
    else:
        print("La opcion no es valida.")

