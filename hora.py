
def Hora():
    print("\n\t\t\t¡Perfecto!""\n\t\t    Has elegido Hora")
    
    print("""\nA continuacion se presentan las unidades a las que se puede convertir:
    \t\t--------------------
    \t\t| 1 |  Segundos    |
    \t\t| 2 |   Minuto     |
    \t\t| 3 |    Día       |
    \t\t| 4 |   Semana     |
    \t\t| 5 |    Mes       |
    \t\t| 6 |    Año       |
    \t\t| 7 |  Bisiesto    |
    \t\t--------------------
    """)

    Num = float(input("¿Que cantidad deseas convertir?: "))

    print("\n¿A que valor deseas convertir las horas?")
    Unidad = input("Escribe la unidad (Primera letra en mayuscula): ")

#------------------------------------------------------------------------------------------------

    #Diccionario
    Equivalencias = {
        "Segundos": (3600/1),
        "Minutos": (60/1),
        "Dia": (1/24),
        "Semana": (1/168),
        "Mes": (1/730),
        "Año": (1/8760),
        "Bisiesto": (1/8784)
    }   

#------------------------------------------------------------------------------------------------

    #Conversion de horas

    if Unidad == "Minutos":
        if Unidad in Equivalencias:
            Minute = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} horas a {Unidad} es: {Minute}\n\n")

    elif Unidad == "Segundos":
        if Unidad in Equivalencias:
            Second= Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} horas a {Unidad} es: {Second}\n\n") 

    elif Unidad == "Dia":
        if Unidad in Equivalencias:
            Day = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} horas a {Unidad} es: {Day}\n\n")   

    elif Unidad == "Semana":
        if Unidad in Equivalencias:
            Week = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} horas a {Unidad} es: {Week}\n\n")

    elif Unidad == "Mes":
        if Unidad in Equivalencias:
            Month = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} horas a {Unidad} es: {Month}\n\n")

    elif Unidad == "Año":
        if Unidad in Equivalencias:
            Year = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} horas a {Unidad} es: {Year}\n\n")

    elif Unidad == "Bisiesto":
        if Unidad in Equivalencias:
            Bisiesto = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido e {Num} horas a {Unidad} es: {Bisiesto}\n\n")

    else:
        print("\n\nLo siento, los datos que has ingresado son invalidos\n\n")
    return