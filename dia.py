
def Dia():
    print("\n\t\t¡Perfecto!""\n\t     Has elegido Dia")
    
    print("""\nA continuacion se presentan las unidades a las que se puede convertir:
    \t\t--------------------
    \t\t| 1 |  Segundos    |
    \t\t| 2 |   Minutos    |
    \t\t| 3 |    Hora      |
    \t\t| 4 |   Semana     |
    \t\t| 5 |    Mes       |
    \t\t| 6 |    Año       |
    \t\t| 7 |  Bisiesto    |
    \t\t--------------------
    """)

    Num = float(input("¿Que cantidad deseas convertir?: "))

    print("\n¿A que valor deseas convertir los dias?")
    Unidad = input("Escribe la unidad (Primera letra en mayuscula): ")

#------------------------------------------------------------------------------------------------

    #Diccionario
    Equivalencias = {
        "Segundos": (86400/1),
        "Minutos": (1440/1),
        "Hora": (24/1),
        "Semana": (1/7),
        "Mes": (1/30.417),
        "Año": (1/365),
        "Bisiesto": (1/366)
    }   

#------------------------------------------------------------------------------------------------

    #Conversion de dias

    if Unidad == "Minutos":
        if Unidad in Equivalencias:
            Minute = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} dias a {Unidad} es: {Minute}\n\n")

    elif Unidad == "Hora":
        if Unidad in Equivalencias:
            Hour = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} dias a {Unidad} es: {Hour}\n\n") 

    elif Unidad == "Segundos":
        if Unidad in Equivalencias:
            Second = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} dias a {Unidad} es: {Second}\n\n")   

    elif Unidad == "Semana":
        if Unidad in Equivalencias:
            Week = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} dias a {Unidad} es: {Week}\n\n")

    elif Unidad == "Mes":
        if Unidad in Equivalencias:
            Month = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} dias a {Unidad} es: {Month}\n\n")

    elif Unidad == "Año":
        if Unidad in Equivalencias:
            Year = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} dias a {Unidad} es: {Year}\n\n")

    elif Unidad == "Bisiesto":
        if Unidad in Equivalencias:
            Bisiesto = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} dias a {Unidad} es: {Bisiesto}\n\n")

    else:
        print("\n\nLo siento, los datos que has ingresado son invalidos\n\n")
    return