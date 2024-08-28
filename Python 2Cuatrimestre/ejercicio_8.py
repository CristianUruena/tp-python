numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("El numero: ", numero, "es divisible por 4")
elif numero % 6 == 0:
    print("El numero: ", numero, "es divisible por 6")
elif numero % 8 == 0:
    print("El numero: ", numero, "es divisible por 8")
elif numero % 10 == 0:
    print("El numero: ", numero, "es divisible por 10")
else:
    print("El numero: ", numero, "no es divisible por 4, 6, 8 o 10")
