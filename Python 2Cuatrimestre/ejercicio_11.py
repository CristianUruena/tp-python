def numero_perfecto(n):
    suma_divisores = 0

    for i in range(1, n): 
        if n % i == 0:  
            suma_divisores += i  
    return suma_divisores == n

numero = int(input("Introduce un número: "))

if numero_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
