
def Bisiesto():
    print("\n\t\t\t¡Perfecto!""\n\t\t  Has elegido Bisiesto")
    
    print("""\nA continuacion se presentan las unidades a las que se puede convertir:
    \t\t--------------------
    \t\t| 1 |   Segundos   |
    \t\t| 2 |   Minutos    |
    \t\t| 3 |     Hora     |
    \t\t| 4 |     Dia      |
    \t\t| 5 |   Semana     |
    \t\t| 6 |     Mes      |
    \t\t--------------------
    """)

    Num = float(input("¿Que cantidad deseas convertir?: "))

    print("\n¿A que valor deseas convertir el año bisiesto?")
    Unidad = input("Escribe la unidad (Primera letra en mayuscula): ")

    #Diccionario
    Equivalencias = {
        "Segundos": (3.162E+7/1),
        "Minutos": (527040/1),
        "Hora": (8784/1),
        "Dia": (366/1),
        "Semana": (52.286/1),
        "Mes": (12.033/1)
    }   

    #Conversion de segundos

    if Unidad == "Minutos":
        if Unidad in Equivalencias:
            Minute = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} año bisiesto a {Unidad} es: {Minute}\n\n")

    elif Unidad == "Hora":
        if Unidad in Equivalencias:
            Hour = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} año bisiesto a {Unidad} es: {Hour}\n\n") 

    elif Unidad == "Dia":
        if Unidad in Equivalencias:
            Day = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} año bisiesto a {Unidad} es: {Day}\n\n")   

    elif Unidad == "Semana":
        if Unidad in Equivalencias:
            Week = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} año bisiesto a {Unidad} es: {Week}\n\n")

    elif Unidad == "Mes":
        if Unidad in Equivalencias:
            Month = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} año bisiesto a {Unidad} es: {Month}\n\n")

    elif Unidad == "Segundos":
        if Unidad in Equivalencias:
            Second = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} año bisiesto a {Unidad} es: {Second}\n\n")

    else:
        print("\n\nLo siento, los datos que has ingresado son invalidos\n\n")
    return