calificacion = int(input("Ingrese su calificacion(0-10): "))

if calificacion >= 0 and calificacion <= 2:
    print('"Muy Malo"')
elif calificacion >= 3 and calificacion <= 4:
    print('"Malo"')
elif calificacion >= 5 and calificacion <= 6:
    print('"Regular"')
elif calificacion >= 7 and calificacion <= 8:
    print('"Muy Bueno"')
elif calificacion >= 9 and calificacion <= 10:
    print('"Exelente"')
else:
    print("Ingrese una calificacion valida")