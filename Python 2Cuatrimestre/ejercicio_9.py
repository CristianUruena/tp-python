numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("El numero: ", numero, "es divisible por 4")
if numero % 6 == 0:
    print("El numero: ", numero, "es divisible por 6")
if numero % 8 == 0:
    print("El numero: ", numero, "es divisible por 8")
if numero % 10 == 0:
    print("El numero: ", numero, "es divisible por 10")

if numero % 4 != 0 and numero % 6 != 0 and numero % 8 != 0 and numero % 10 != 0:
    print(f"El numero: {numero} no es divisible por 4, 6, 8, 10")
