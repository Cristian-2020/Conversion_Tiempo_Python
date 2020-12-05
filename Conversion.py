#Conversor de unidades del sistema SI (Tiempo)

print("\t---------------------------------------------------")
print("\t\tConversor de Unidades S.I (Tiempo)")
print("\t---------------------------------------------------\n")

print("\t\t\tBienvenido\n""En este nuevo programa realizaremos conversiones de unidades de tiempo\n")

#-------------------------------------------------------------------------------------------------------

print("""\tLas unidades soportadas por este programas son:
\t\t----------------------------------
\t\t|   Segundos   |    Semana       |
\t\t|   Minutos    |      Mes        |
\t\t|    Hora      |     Años        |
\t\t|     Dia      |   Bisiesto      |
\t\t----------------------------------

\t\t\tPasos:
1 - Primero deberas escribir la unidad que deseas convertir (Para segundos y minutos debe ir en plural)
2-  Despues digita el valor que deseas convertir
3 - Luego tendras que seleccionar en que unidad deseas que se muestre
4 - Veras el resultado

 ------------------------------------------------------------------------
|Nota: Si deseas volver a intentarlo, deberas volver a correr el programa|
 ------------------------------------------------------------------------

\t\t\t¡Empezemos!
""")

#------------------------------------------------------------------------------------------------------

Seleccion = input("¿Que unidad deseas convertir?: ")

if Seleccion == "Segundos" or Seleccion == "segundos":
    from segundos import*
    Segundos()

elif Seleccion == "Minutos" or Seleccion == "minutos":
    from minutos import*
    Minutos()

elif Seleccion == "Hora" or Seleccion == "hora":
    from hora import*
    Hora()

elif Seleccion == "Dia" or Seleccion == "dia":
    from dia import*
    Dia()

elif Seleccion == "Semana" or Seleccion == "semana":
    from semana import*
    Semana()

elif Seleccion == "Mes" or Seleccion == "mes":
    from mes import*
    Mes()

elif Seleccion == "Año" or Seleccion == "año":
    from año import*
    Año()

elif Seleccion == "Bisiesto" or Seleccion == "bisiesto":
    from bisiesto import*
    Bisiesto()

else:    
    print("\nLo sentimos, el dato ingresado es invalido\n")

#---------------------------------------------------------------------------------------------------

print("\t---------------------------------------------------")
print("\t\tGracias por usar nuestro programa")
print("\t---------------------------------------------------")