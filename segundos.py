
def Segundos():
    print("\n\t\t\t ¡Perfecto!""\n\t\t    Has elegido Segundos")
    
    print("""\nA continuacion se presentan las unidades a las que se puede convertir:
    \t\t--------------------
    \t\t| 1 |   Minutos    |
    \t\t| 2 |    Hora      |
    \t\t| 3 |    Día       |
    \t\t| 4 |   Semana     |
    \t\t| 5 |    Mes       |
    \t\t| 6 |    Año       |
    \t\t| 7 |  Bisiesto    |
    \t\t--------------------
    """)

    Num = float(input("¿Que cantidad deseas convertir?: "))

    print("\n¿A que valor deseas convertir los segundos?")
    Unidad = input("Escribe la unidad (Primera letra en mayuscula): ")

#------------------------------------------------------------------------------------------------

    #Diccionario
    Equivalencias = {
        "Minutos": (1/60),
        "Hora": (1/3600),
        "Dia": (1/86400),
        "Semana": (1/604800),
        "Mes": (1/2.628E+6),
        "Año": (1/3.154E+7),
        "Bisiesto": (1/3.162E+7)
    }   

#------------------------------------------------------------------------------------------------

    #Conversion de segundos

    if Unidad == "Minutos":
        if Unidad in Equivalencias:
            Minute = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} segundos a {Unidad} es: {Minute}\n\n")

    elif Unidad == "Hora":
        if Unidad in Equivalencias:
            Hour = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} segundos a {Unidad} es: {Hour}\n\n") 

    elif Unidad == "Dia":
        if Unidad in Equivalencias:
            Day = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} segundos a {Unidad} es: {Day}\n\n")   

    elif Unidad == "Semana":
        if Unidad in Equivalencias:
            Week = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} segundos a {Unidad} es: {Week}\n\n")

    elif Unidad == "Mes":
        if Unidad in Equivalencias:
            Month = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} segundos a {Unidad} es: {Month}\n\n")

    elif Unidad == "Año":
        if Unidad in Equivalencias:
            Year = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} segundos a {Unidad} es: {Year}\n\n")

    elif Unidad == "Bisiesto":
        if Unidad in Equivalencias:
            Bisiesto = Num * Equivalencias[Unidad]
            print(f"\n\nEl valor convertido de {Num} segundos a {Unidad} es: {Bisiesto}\n\n")
    else:
        print("\n\nLo siento, los datos que has ingresado son invalidos\n\n")
    return