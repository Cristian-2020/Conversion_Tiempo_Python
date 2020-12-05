
def Mes():
    print("\n\t\t\t¡Perfecto!""\n\t\t  Has elegido Mes")
    
    print("""\nA continuacion se presentan las unidades a las que se puede convertir:
    \t\t---------------------
    \t\t| 1 |   Segundos    |
    \t\t| 2 |   Minutos     |
    \t\t| 3 |    Hora       |
    \t\t| 4 |     Dia       |
    \t\t| 5 |   Semana      |
    \t\t| 6 |     Año       |
    \t\t| 7 |   Bisiesto    |
    \t\t---------------------
    """)

    Num = float(input("¿Que cantidad deseas convertir?: "))

    print("\n¿A que valor deseas convertir el mes?")
    Unidad = input("Escribe la unidad (Primera letra en mayuscula): ")

    #Diccionario
    Equivalencias = {
        "Segundos": (2.628E+6/1),
        "Minutos": (43800),
        "Hora": (730/1),
        "Dia": (30.417/1),
        "Semana": (4.345/1),
        "Año": (1/12),
        "Bisiesto": (1/12.033)
    }   

    #Conversion de meses

    if Unidad == "Minutos":
        if Unidad in Equivalencias:
            Minute = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} meses a {Unidad} es: {Minute}\n\n")

    elif Unidad == "Hora":
        if Unidad in Equivalencias:
            Hour = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} meses a {Unidad} es: {Hour}\n\n") 

    elif Unidad == "Dia":
        if Unidad in Equivalencias:
            Day = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} meses a {Unidad} es: {Day}\n\n")   

    elif Unidad == "Semana":
        if Unidad in Equivalencias:
            Week = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} meses a {Unidad} es: {Week}\n\n")

    elif Unidad == "Segundos":
        if Unidad in Equivalencias:
            Second = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} meses a {Unidad} es: {Second}\n\n")

    elif Unidad == "Año":
        if Unidad in Equivalencias:
            Year = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} meses a {Unidad} es: {Year}\n\n")

    elif Unidad == "Bisiesto":
        if Unidad in Equivalencias:
            Bisiesto = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} meses a {Unidad} es: {Bisiesto}\n\n")

    else:
        print("\n\nLo siento, los datos que has ingresado son invalidos\n\n")
    return