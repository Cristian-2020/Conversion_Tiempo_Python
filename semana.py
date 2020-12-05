
def Semana():
    print("\n\t\t\t¡Perfecto!""\n\t\t  Has elegido Semana")
    
    print("""\nA continuacion se presentan las unidades a las que se puede convertir:
    \t\t---------------------
    \t\t| 1 |   Segundos    |
    \t\t| 2 |   Minutos     |
    \t\t| 3 |    Hora       |
    \t\t| 4 |     Dia       |
    \t\t| 5 |     Mes       |
    \t\t| 6 |     Año       |
    \t\t| 7 |   Bisiesto    |
    \t\t---------------------
    """)

    Num = float(input("¿Que cantidad deseas convertir?: "))

    print("\n¿A que valor deseas convertir la semana?")
    Unidad = input("Escribe la unidad (Primera letra en mayuscula): ")

#------------------------------------------------------------------------------------------------

    #Diccionario
    Equivalencias = {
        "Segundos": (604800/1),
        "Minutos": (10080/1),
        "Hora": (168/1),
        "Dia": (7/1),
        "Mes": (1/4.345),
        "Año": (1/52.143),
        "Bisiesto": (1/0.0191257)
    }   

#------------------------------------------------------------------------------------------------

    #Conversion de semanas

    if Unidad == "Minutos":
        if Unidad in Equivalencias:
            Minute = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} semanas a {Unidad} es: {Minute}\n\n")

    elif Unidad == "Hora":
        if Unidad in Equivalencias:
            Hour = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} semanas a {Unidad} es: {Hour}\n\n") 

    elif Unidad == "Dia":
        if Unidad in Equivalencias:
            Day = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} semanas a {Unidad} es: {Day}\n\n")   

    elif Unidad == "Segundos":
        if Unidad in Equivalencias:
            Second = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} semanas a {Unidad} es: {Second}\n\n")

    elif Unidad == "Mes":
        if Unidad in Equivalencias:
            Month = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} semanas a {Unidad} es: {Month}\n\n")

    elif Unidad == "Año":
        if Unidad in Equivalencias:
            Year = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} semanas a {Unidad} es: {Year}\n\n")

    elif Unidad == "Bisiesto":
        if Unidad in Equivalencias:
            Bisiesto = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} semanas a {Unidad} es: {Bisiesto}\n\n")

    else:
        print("\n\nLo siento, los datos que has ingresado son invalidos\n\n")
    return