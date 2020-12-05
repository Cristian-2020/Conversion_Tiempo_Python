
def Minutos():
    print("\n\t\t\t¡Perfecto!""\n\t\t    Has elegido Minuto")
    
    print("""\nA continuacion se presentan las unidades a las que se puede convertir:
    \t\t--------------------
    \t\t| 1 |  Segundos    |
    \t\t| 2 |    Hora      |
    \t\t| 3 |    Día       |
    \t\t| 4 |   Semana     |
    \t\t| 5 |    Mes       |
    \t\t| 6 |    Año       |
    \t\t| 7 |  Bisiesto    |
    \t\t--------------------
    """)

    Num = float(input("¿Que cantidad deseas convertir?: "))

    print("\n¿A que valor deseas convertir los minutos?")
    Unidad = input("Escribe la unidad (Primera letra en mayuscula): ")

#------------------------------------------------------------------------------------------------

    #Diccionario
    Equivalencias = {
        "Segundos": (60/1),
        "Hora": (1/60),
        "Dia": (1/1440),
        "Semana": (1/10080),
        "Mes": (1/43800),
        "Año": (1/525600),
        "Bisiesto": (1/527040)
    }   

#------------------------------------------------------------------------------------------------

    #Conversion de minutos

    if Unidad == "Segundos":
        if Unidad in Equivalencias:
            Second = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} minutos a {Unidad} es: {Second}\n\n")

    elif Unidad == "Hora":
        if Unidad in Equivalencias:
            Hour = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} minutos a {Unidad} es: {Hour}\n\n") 

    elif Unidad == "Dia":
        if Unidad in Equivalencias:
            Day = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} minutos a {Unidad} es: {Day}\n\n")   

    elif Unidad == "Semana":
        if Unidad in Equivalencias:
            Week = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} minutos a {Unidad} es: {Week}\n\n")

    elif Unidad == "Mes":
        if Unidad in Equivalencias:
            Month = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} minutos a {Unidad} es: {Month}\n\n")

    elif Unidad == "Año":
        if Unidad in Equivalencias:
            Year = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} minutos a {Unidad} es: {Year}\n\n")

    elif Unidad == "Bisiesto":
        if Unidad in Equivalencias:
            Bisiesto = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} minutos a {Unidad} es: {Bisiesto}\n\n")

    else:
        print("\n\nLo siento, los datos que has ingresado son invalidos\n\n")
    return