def ingresar_numeros():
    cantidad = input("Ingrese la cantidad de números que desea operar: ")

    while not cantidad.isdigit():
        print("Por favor, ingrese un número válido.")
        cantidad = input("Ingrese la cantidad de números que desea operar: ")

    cantidad = int(cantidad)

    numeros = []

    for i in range(cantidad):
        numero = input(f"Ingrese el número {i + 1}: ")

        while not numero.replace(".", "", 1).isdigit():
            print("Por favor, ingrese un número válido.")
            numero = input(f"Ingrese el número {i + 1}: ")

        numeros.append(numero)

    return numeros

numeros_ingresados = ingresar_numeros()
print("Números ingresados:", numeros_ingresados)
