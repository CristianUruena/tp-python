def imprimir_numeros():
    for i in range(1, 301):
        output = str(i)  
        
        if i % 5 == 0:
            output += " (Múltiplo de 5)"

        if i % 7 == 0:
            output += " (Múltiplo de 7)"
            print(output)  

        if i % 6 == 0:
            print("------------------------------------------------------------")

imprimir_numeros()
